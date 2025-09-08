import socket
import math
import random

# ========================== 설정 ==========================
NICKNAME = 'hi'
HOST = '127.0.0.1'
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
BALL_RADIUS = 2.87
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
EPS = 0.01

# ========================== 초기화 ==========================
order = 0
balls = [[-1, -1] for _ in range(NUMBER_OF_BALLS)]

sock = socket.socket()
sock.connect((HOST, PORT))
sock.send(f'{CODE_SEND}/{NICKNAME}'.encode())
print('Connected and Ready to Play!\n--------------------')

# ========================== 함수 ==========================
def select_target(balls, order):
    """존재하는 목적구 선택"""
    target_order = {1: [3, 1, 5], 2: [4, 2, 5]}
    for idx in target_order[order]:
        if balls[idx][0] >= 0 and balls[idx][1] >= 0:
            return idx
    return None

def select_hole(target_x, target_y):
    """가장 가까운 홀 선택"""
    best_hole = None
    min_dist = float('inf')
    for hx, hy in HOLES:
        dist = math.hypot(target_x - hx, target_y - hy)
        if dist < min_dist:
            min_dist = dist
            best_hole = (hx, hy)
    return best_hole

def calc_shot(white_x, white_y, target_x, target_y, hole_x, hole_y):
    """각도와 파워 계산"""
    dx_hole = hole_x - target_x
    dy_hole = hole_y - target_y
    dist_hole = max(math.hypot(dx_hole, dy_hole), EPS)

    # 목적구 충돌 위치
    offset_x = target_x - dx_hole * BALL_RADIUS * 2 / dist_hole
    offset_y = target_y - dy_hole * BALL_RADIUS * 2 / dist_hole

    dx = offset_x - white_x
    dy = offset_y - white_y
    angle = math.degrees(math.atan2(dy, dx))
    if angle < 0:
        angle += 360

    # 거리 기반 파워 계산
    dist1 = math.hypot(dx, dy)
    dist2 = dist_hole
    power = (dist1 + dist2) * 0.9  # 계수 조절
    power = max(25, min(power, 100))
    return angle, power

def safe_shot(angle):
    """안전샷 각도 약간 랜덤 조정"""
    offset = random.uniform(-5, 5)
    angle += offset
    angle %= 360
    return angle

# ========================== 메인 루프 ==========================
while True:
    try:
        recv_data = sock.recv(1024).decode()
        split_data = recv_data.split('/')
        idx = 0
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        sock.send(f'{CODE_REQUEST}/{NICKNAME}'.encode())
        continue

    # 순서/종료 확인
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print(f'\n* You will be the {"first" if order==1 else "second"} player. *\n')
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    white_x, white_y = balls[0]
    target_idx = select_target(balls, order)

    if target_idx is not None:
        target_x, target_y = balls[target_idx]
        hole_x, hole_y = select_hole(target_x, target_y)
        angle, power = calc_shot(white_x, white_y, target_x, target_y, hole_x, hole_y)
        angle = safe_shot(angle)
    else:
        # 목적구 없으면 안전샷
        angle = 180 if white_x < TABLE_WIDTH / 2 else 0
        angle = safe_shot(angle)
        power = 30

    merged_data = f'{angle}/{power}/'
    sock.send(merged_data.encode())
    print(f'Shot Sent -> Angle: {angle:.2f}, Power: {power:.2f}')

sock.close()
print('Connection Closed.\n--------------------')
