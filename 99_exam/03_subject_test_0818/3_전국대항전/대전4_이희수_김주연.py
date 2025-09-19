import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '대전4_이희수_김주연'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경 상수
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

# 당구공 파라미터(경험치)
BALL_DIAMETER = 5.73
BALL_RADIUS = BALL_DIAMETER / 2
# 유령점 오프셋 : 타깃→포켓 방향으로 지름 1배만큼 뒤
GHOST_BACK = BALL_DIAMETER * 1.00
# 유령점이 쿠션 가까우면 약간 덜 물리는 보정(쿠션 끼임 방지)
GHOST_WALL_RELAX = 0.85

# 파워 범위
MIN_PWR = 32.0
MAX_PWR = 100.0

# 차단(끼어들기) 판정 허용 오차
BLOCK_TOL = BALL_RADIUS * 0.9  # 선거리 허용

order = 0
balls = [[0, 0] for _ in range(NUMBER_OF_BALLS)]

# ----------------- 유틸 -----------------
def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def is_alive(x, y):
    # 포켓된 공은 -1/-1. 약간의 여유 허용
    return -0.5 <= x <= TABLE_WIDTH + 0.5 and -0.5 <= y <= TABLE_HEIGHT + 0.5

def angle_from_delta(dx, dy):
    # 일타싸피: 아래(+y)가 0°, 시계방향 증가
    return (math.degrees(math.atan2(dx, dy)) + 360.0) % 360.0

def dist(a, b, c, d):
    return math.hypot(c - a, d - b)

def unit_vec(dx, dy):
    L = math.hypot(dx, dy)
    if L < 1e-9:
        return 0.0, 0.0, 0.0
    return dx / L, dy / L, L

def line_point_distance(ax, ay, bx, by, px, py):
    """ 선분 AB 에서 점 P까지 최소 거리와, 투영비 t(0~1 범위 내면 선분 내부) """
    vx, vy = bx - ax, by - ay
    wx, wy = px - ax, py - ay
    vv = vx * vx + vy * vy
    if vv < 1e-9:
        return math.hypot(wx, wy), 0.0
    t = (wx * vx + wy * vy) / vv
    t_clamped = clamp(t, 0.0, 1.0)
    qx, qy = ax + t_clamped * vx, ay + t_clamped * vy
    return math.hypot(px - qx, py - qy), t

def near_cushion(x, y, margin=BALL_RADIUS*1.2):
    return (x < margin) or (x > TABLE_WIDTH - margin) or (y < margin) or (y > TABLE_HEIGHT - margin)

# --------- 각도 정교화 핵심 로직 ----------
def ghost_point_for_pocket(tx, ty, hx, hy):
    """ 타깃(tx,ty)에서 포켓(hx,hy) 방향으로 유닛벡터 얻고, 그 반대방향으로 GHOST_BACK 만큼 물린 지점을 유령점으로 """
    ux, uy, L = unit_vec(hx - tx, hy - ty)
    if L < 1e-6:
        return tx, ty  # 예외: 동일점
    back = GHOST_BACK
    # 포켓이 쿠션 모서리/벽에 가까우면 유령을 덜 물려서 끼임 줄임
    if near_cushion(tx, ty) or near_cushion(hx, hy):
        back *= GHOST_WALL_RELAX
    gx, gy = tx - ux * back, ty - uy * back
    # 테이블 밖으로 나가면 타깃 중심 조준
    if not (0 <= gx <= TABLE_WIDTH and 0 <= gy <= TABLE_HEIGHT):
        gx, gy = tx, ty
    return gx, gy

def shot_blocked(white_x, white_y, aim_x, aim_y, ignore_indices):
    """ 큐볼→유령점 경로에 다른 공이 끼어드는지 판정 """
    for i in range(1, NUMBER_OF_BALLS):
        if i in ignore_indices:
            continue
        bx, by = balls[i][0], balls[i][1]
        if not is_alive(bx, by):
            continue
        dmin, t = line_point_distance(white_x, white_y, aim_x, aim_y, bx, by)
        # 유령점 바로 앞 구간(마지막 1.0~0.0 중 0.1이내)은 충돌로 보지 않음(접점 근처 노이즈)
        if dmin <= BLOCK_TOL and (0.0 <= t <= 0.9):
            return True
    return False

def pick_best_pocket_by_cut(white_x, white_y, tx, ty):
    """
    포켓 후보들 중
    1) 유령점 경로가 차단되지 않고
    2) 컷 각도(큐볼-타깃 선 vs 타깃-포켓 선)가 작은 것
    을 우선 선택.
    반환: (선택 포켓 좌표 hx,hy, 유령점 gx,gy) 또는 None
    """
    # 큐볼->타깃 벡터
    cux, cuy, Lct = unit_vec(tx - white_x, ty - white_y)
    if Lct < 1e-6:
        return None

    best = None
    best_score = 1e18

    for hx, hy in HOLES:
        # 유령점 후보
        gx, gy = ghost_point_for_pocket(tx, ty, hx, hy)

        # 컷 각도 = (타깃->포켓) 과 (큐볼->타깃) 의 각도 차
        tux, tuy, _ = unit_vec(hx - tx, hy - ty)
        dot = clamp(cux * tux + cuy * tuy, -1.0, 1.0)
        cut_deg = math.degrees(math.acos(dot))  # 0°가 직진, 커질수록 어려운 컷

        # 경로 차단 확인 (큐볼→유령점). 타깃 공 자체는 무시해야 하므로 ignore 목록에 포함
        blocked = shot_blocked(white_x, white_y, gx, gy, ignore_indices={0, })  # 0은 큐볼, 타깃은 무시 안 해도 유령점-타깃 겹쳐 고려 말단 제외
        # 차단되면 페널티 크게
        penalty = 1000.0 if blocked else 0.0

        # 포켓과 타깃 거리도 가중(너무 먼 포켓은 조금 불리)
        t2h = dist(tx, ty, hx, hy)
        score = cut_deg + penalty + (t2h * 0.03)

        if score < best_score:
            best_score = score
            best = (hx, hy, gx, gy)

    return best

# ===== 일직선 우선 선택 =====
ANGLE_TOL = 4.0                        # 직선 정렬 각도 허용치(도)
COLLINEAR_DIST_TOL = BALL_RADIUS * 0.9 # 타깃이 선분(흰→홀) 위 허용 오차

def aligned_choice_first(white_x, white_y, targets):
    """
    흰공-타깃-홀 이 거의 일직선이면 그 타깃/홀 조합을 우선 반환.
    반환: (target_idx, hx, hy, gx, gy) 또는 None
    """
    best = None
    best_score = 1e18
    for ti in targets:
        tx, ty = balls[ti][0], balls[ti][1]
        if not is_alive(tx, ty):
            continue
        for hx, hy in HOLES:
            # 흰→타깃 vs 흰→홀 방향 각도
            ux1, uy1, L1 = unit_vec(tx - white_x, ty - white_y)
            ux2, uy2, L2 = unit_vec(hx - white_x, hy - white_y)
            if L1 < 1e-6 or L2 < 1e-6:
                continue
            dot = clamp(ux1 * ux2 + uy1 * uy2, -1.0, 1.0)
            ang = math.degrees(math.acos(dot))
            # 타깃이 선분(흰→홀) 위에 놓이는지
            dmin, tproj = line_point_distance(white_x, white_y, hx, hy, tx, ty)
            on_segment = (0.0 < tproj < 1.0) and (dmin <= COLLINEAR_DIST_TOL)
            if ang <= ANGLE_TOL and on_segment:
                gx, gy = ghost_point_for_pocket(tx, ty, hx, hy)
                # 유령점 경로 차단 없어야 함(타깃은 무시)
                if not shot_blocked(white_x, white_y, gx, gy, ignore_indices={0, ti}):
                    score = ang + dmin * 2.0 + dist(white_x, white_y, tx, ty) * 0.02
                    if score < best_score:
                        best_score = score
                        best = (ti, hx, hy, gx, gy)
    return best

# -----------------------------------------

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

while True:
    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 50.0  # 안전 기본값

    ##############################
    # ===== 여기서부터 전략 로직 =====

    white_x, white_y = balls[0][0], balls[0][1]

    # 5번 공(8번 공)은 항상 마지막(대체)만 고려
    primary_idx = [1, 3] if order == 1 else [2, 4]

    alive_primary = []
    for idx_ball in primary_idx:
        tx, ty = balls[idx_ball][0], balls[idx_ball][1]
        if is_alive(tx, ty):
            alive_primary.append(idx_ball)

    alive_targets = alive_primary if alive_primary else []
    if not alive_targets:
        # 1차 타깃이 없을 때만 5번 공 고려
        tx5, ty5 = balls[5][0], balls[5][1]
        if is_alive(tx5, ty5):
            alive_targets = [5]

    if alive_targets:
        # ★ 추가: 일직선 정렬 타깃을 최우선으로 선택
        aligned = aligned_choice_first(white_x, white_y, alive_targets)

        if aligned is not None:
            target_idx, hx, hy, gx, gy = aligned
            tx, ty = balls[target_idx][0], balls[target_idx][1]
        else:
            # 기존 로직: 흰공과 가장 가까운 타깃 1개 선택
            target_idx = min(alive_targets, key=lambda i: dist(white_x, white_y, balls[i][0], balls[i][1]))
            tx, ty = balls[target_idx][0], balls[target_idx][1]

            # 포켓 선택: 컷 각도 최소 + 경로 차단 회피
            choice = pick_best_pocket_by_cut(white_x, white_y, tx, ty)
            if choice is None:
                # 백업: 타깃에서 가장 가까운 포켓으로 유령점 생성
                hx, hy = min(HOLES, key=lambda h: dist(tx, ty, h[0], h[1]))
                gx, gy = ghost_point_for_pocket(tx, ty, hx, hy)
            else:
                hx, hy, gx, gy = choice

        # 최종 각도: 큐볼 → 유령점
        dx, dy = gx - white_x, gy - white_y
        angle = angle_from_delta(dx, dy)

        # 파워: 거리 기반 + 포켓 거리 보정(멀수록 약간 더)
        dist_q = math.hypot(dx, dy)
        d_th = dist(tx, ty, hx, hy)
        base_scale = 0.62 + 0.16 * clamp(d_th / 150.0, 0.0, 1.0)
        power = clamp(dist_q * base_scale, MIN_PWR, MAX_PWR)

        # 아주 가까우면 최소 파워 보장
        if dist_q < 2.5 * BALL_RADIUS:
            power = max(power, MIN_PWR + 2.0)
    else:
        # 타깃 없거나 인식 불가: 중앙으로 기본샷
        cx, cy = TABLE_WIDTH / 2, TABLE_HEIGHT / 2
        dx, dy = cx - white_x, cy - white_y
        angle = angle_from_delta(dx, dy)
        dist_q = math.hypot(dx, dy)
        power = clamp(dist_q * 0.7, MIN_PWR, MAX_PWR)

    # ===== 전략 로직 끝 =====
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')