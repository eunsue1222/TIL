import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '대전_4반_김가영'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

# 공의 반지름 (당구공 표준 크기)
BALL_RADIUS = 5.73 / 2

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


def distance_point_to_line(px, py, x1, y1, x2, y2):
    """점에서 직선까지의 최단거리를 계산"""
    A = px - x1
    B = py - y1
    C = x2 - x1
    D = y2 - y1

    dot = A * C + B * D
    len_sq = C * C + D * D

    if len_sq == 0:
        return math.sqrt(A * A + B * B)

    param = dot / len_sq

    if param < 0:
        xx = x1
        yy = y1
    elif param > 1:
        xx = x2
        yy = y2
    else:
        xx = x1 + param * C
        yy = y1 + param * D

    dx = px - xx
    dy = py - yy
    return math.sqrt(dx * dx + dy * dy)


def check_path_collision(start_pos, end_pos, balls, ignore_indices=None):
    """경로상에 다른 공이 있는지 확인"""
    if ignore_indices is None:
        ignore_indices = []

    start_x, start_y = start_pos
    end_x, end_y = end_pos

    colliding_balls = []

    for i in range(NUMBER_OF_BALLS):
        if i in ignore_indices or balls[i][0] < 0:
            continue

        ball_x, ball_y = balls[i][0], balls[i][1]

        distance = distance_point_to_line(ball_x, ball_y, start_x, start_y, end_x, end_y)
        if distance < BALL_RADIUS * 2.2:
            colliding_balls.append(i)

    return colliding_balls


def calculate_cut_shot(white_pos, target_pos, hole_pos):
    """빗겨치기(컷 샷)를 위한 각도 계산 - 삼각함수 및 제2코사인법칙 사용"""
    white_x, white_y = white_pos
    target_x, target_y = target_pos
    hole_x, hole_y = hole_pos

    target_to_hole_x = hole_x - target_x
    target_to_hole_y = hole_y - target_y
    target_to_hole_dist = math.sqrt(target_to_hole_x ** 2 + target_to_hole_y ** 2)

    if target_to_hole_dist == 0:
        return None, None

    target_dir_x = target_to_hole_x / target_to_hole_dist
    target_dir_y = target_to_hole_y / target_to_hole_dist

    white_to_target_x = target_x - white_x
    white_to_target_y = target_y - white_y
    white_to_target_dist = math.sqrt(white_to_target_x ** 2 + white_to_target_y ** 2)

    if white_to_target_dist == 0:
        return None, None

    contact_x = target_x - target_dir_x * BALL_RADIUS * 2
    contact_y = target_y - target_dir_y * BALL_RADIUS * 2

    aim_x = contact_x - white_x
    aim_y = contact_y - white_y

    if aim_x == 0:
        angle = 0 if aim_y > 0 else 180
    elif aim_y == 0:
        angle = 90 if aim_x > 0 else 270
    else:
        radian = math.atan2(aim_x, aim_y)
        angle = math.degrees(radian)
        if angle < 0:
            angle += 360

    white_to_target_angle = math.atan2(white_to_target_x, white_to_target_y)
    target_direction_angle = math.atan2(target_to_hole_y, target_to_hole_x)

    cut_angle = abs(white_to_target_angle - target_direction_angle)
    if cut_angle > math.pi:
        cut_angle = 2 * math.pi - cut_angle

    cut_efficiency = abs(math.cos(cut_angle)) if cut_angle < math.pi / 2 else 0.3

    return angle, cut_efficiency, cut_angle


def find_closest_hole(x, y):
    """가장 가까운 홀을 찾는 함수"""
    min_distance = float('inf')
    closest_hole = None

    for hole in HOLES:
        distance = math.sqrt((hole[0] - x) ** 2 + (hole[1] - y) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_hole = hole

    return closest_hole


def find_best_hole_for_cut_shot(white_pos, target_pos, balls, target_idx):
    """빗겨치기를 고려하여 최적의 홀을 찾는 함수"""
    white_x, white_y = white_pos
    target_x, target_y = target_pos

    hole_scores = []

    for hole in HOLES:
        hole_x, hole_y = hole

        result = calculate_cut_shot((white_x, white_y), (target_x, target_y), (hole_x, hole_y))
        if result[0] is None:
            continue

        angle, cut_efficiency, cut_angle = result

        collisions_to_target = check_path_collision(
            (white_x, white_y), (target_x, target_y), balls,
            ignore_indices=[0, target_idx]
        )

        collisions_to_hole = check_path_collision(
            (target_x, target_y), (hole_x, hole_y), balls,
            ignore_indices=[0, target_idx]
        )

        score = 0
        white_to_target_dist = math.sqrt((target_x - white_x) ** 2 + (target_y - white_y) ** 2)
        target_to_hole_dist = math.sqrt((hole_x - target_x) ** 2 + (hole_y - target_y) ** 2)
        score += white_to_target_dist * 0.3
        score += target_to_hole_dist * 0.2

        cut_angle_degrees = math.degrees(cut_angle)
        if cut_angle_degrees > 60:
            score += (cut_angle_degrees - 60) * 2

        score += (1 - cut_efficiency) * 50
        score += len(collisions_to_target) * 200
        score += len(collisions_to_hole) * 100

        hole_scores.append((hole, score, collisions_to_target, collisions_to_hole, cut_angle_degrees, cut_efficiency))

    if not hole_scores:
        return None, [], [], 0, 0

    best_choice = min(hole_scores, key=lambda x: x[1])
    return best_choice[0], best_choice[2], best_choice[3], best_choice[4], best_choice[5]


def get_ball_sequence(order):
    """플레이어별 공 넣는 순서 반환"""
    if order == 1:
        return [1, 3, 5]
    else:
        return [2, 4, 5]


def find_current_target_ball(balls, order):
    """현재 쳐야 할 공을 순서대로 찾기"""
    sequence = get_ball_sequence(order)
    for ball_idx in sequence:
        if balls[ball_idx][0] >= 0:
            return ball_idx
    return None


def check_remaining_balls(balls, order):
    """내가 쳐야 할 공이 남아있는지 확인 (순서 고려)"""
    sequence = get_ball_sequence(order)
    remaining = []
    for ball_idx in sequence:
        if balls[ball_idx][0] >= 0:
            remaining.append(ball_idx)
    return remaining


def find_target_ball(balls, order):
    """순서를 지켜서 타겟 공을 찾는 함수 (순차적 진행)"""
    target_ball = find_current_target_ball(balls, order)
    if target_ball is None:
        print("모든 공을 순서대로 넣었습니다!")
        return None
    elif target_ball == 5:
        print("1,3번(또는 2,4번) 공을 모두 넣었습니다! 8번공을 타겟으로 합니다.")
    return target_ball


def calculate_cut_shot_power(white_pos, target_pos, hole_pos, cut_efficiency):
    """컷샷을 위한 파워 계산"""
    white_x, white_y = white_pos
    target_x, target_y = target_pos
    hole_x, hole_y = hole_pos

    white_to_target_dist = math.sqrt((target_x - white_x) ** 2 + (target_y - white_y) ** 2)
    target_to_hole_dist = math.sqrt((hole_x - target_x) ** 2 + (hole_y - target_y) ** 2)

    base_power = white_to_target_dist * 0.5 + target_to_hole_dist * 0.3
    power_correction = 1.0 / max(cut_efficiency, 0.3)
    final_power = base_power * power_correction
    final_power = min(final_power, 95.0)
    final_power = max(final_power, 20.0)

    return final_power


def calculate_direct_angle_and_power(white_pos, target_pos):
    """(추가) 흰 공에서 목표 공으로 바로 치는 각도와 기본 파워를 계산하는 함수"""
    white_x, white_y = white_pos
    target_x, target_y = target_pos

    # 목표 공을 향하는 방향 벡터 계산
    aim_x = target_x - white_x
    aim_y = target_y - white_y

    # 각도 계산
    radian = math.atan2(aim_x, aim_y)
    angle = math.degrees(radian)
    if angle < 0:
        angle += 360

    # 거리에 따른 기본 파워 계산 (너무 세지 않게)
    distance = math.sqrt(aim_x ** 2 + aim_y ** 2)
    power = distance * 0.4
    power = max(25, min(power, 60))  # 최소 25, 최대 60의 힘으로 제한

    return angle, power


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
    power = 0.0

    ##############################
    # (수정) 컷샷 및 수비샷을 포함한 게임 로직
    ##############################

    # 순서대로 타겟 공 찾기
    target_idx = find_target_ball(balls, order)

    if target_idx is None:
        print("No valid target ball found!")
        # 칠 공이 없으면 안전하게 약하게 침
        angle = 0
        power = 30
    else:
        # 흰 공과 타겟 공의 좌표
        white_x, white_y = balls[0][0], balls[0][1]
        target_x, target_y = balls[target_idx][0], balls[target_idx][1]

        # 1. (플랜 A) 최적의 홀과 컷샷 정보 계산
        result = find_best_hole_for_cut_shot(
            (white_x, white_y), (target_x, target_y), balls, target_idx
        )

        best_hole = result[0]

        # 2. 플랜 A가 실패했는지 확인
        if best_hole is not None:
            # 플랜 A 성공: 컷샷 실행
            print("✅ 플랜 A: 컷 샷을 시도합니다!")
            _, collisions_to_target, collisions_to_hole, cut_angle_deg, cut_efficiency = result

            # 컷샷 각도 계산
            cut_result = calculate_cut_shot(
                (white_x, white_y), (target_x, target_y), best_hole
            )

            angle, _, _ = cut_result
            power = calculate_cut_shot_power(
                (white_x, white_y), (target_x, target_y), best_hole, cut_efficiency
            )

            # 정보 출력
            print('====== 컷샷 정보 ======')
            print(f'Player Order: {order} ({"선공" if order == 1 else "후공"})')
            sequence = get_ball_sequence(order)
            sequence_status = []
            for ball_idx in sequence:
                if balls[ball_idx][0] >= 0:
                    if ball_idx == target_idx:
                        sequence_status.append(f'[{ball_idx}] ← 현재 타겟')
                    else:
                        sequence_status.append(f'{ball_idx}')
                else:
                    sequence_status.append(f'✓{ball_idx}')

            print(f'진행 순서: {" -> ".join(sequence_status)}')
            print(f'Current Target: {target_idx}번 공')
            print(f'흰 공 위치: ({white_x:.2f}, {white_y:.2f})')
            print(f'타겟 공 위치: ({target_x:.2f}, {target_y:.2f})')
            print(f'타겟 홀: ({best_hole[0]}, {best_hole[1]})')
            print(f'컷 각도: {cut_angle_deg:.1f}도')
            print(f'컷 효율: {cut_efficiency:.2f} ({cut_efficiency * 100:.0f}%)')

            if collisions_to_target:
                print(f'⚠️  타격 경로에 방해 공: {collisions_to_target}')
            if collisions_to_hole:
                print(f'⚠️  홀로 가는 경로에 방해 공: {collisions_to_hole}')
            if not collisions_to_target and not collisions_to_hole:
                print('✅ 깨끗한 컷샷 경로!')

            if cut_angle_deg < 30:
                print('🟢 쉬운 컷샷')
            elif cut_angle_deg < 45:
                print('🟡 보통 컷샷')
            elif cut_angle_deg < 60:
                print('🟠 어려운 컷샷')
            else:
                print('🔴 매우 어려운 컷샷')
            print('====================')

            print(f'계산된 각도: {angle:.2f}도')
            print(f'계산된 파워: {power:.2f}')

        else:
            # 3. (플랜 B) 수비 샷 실행
            print("⚠️ 플랜 A 실패! 플랜 B: 수비 샷으로 전환합니다.")

            angle, power = calculate_direct_angle_and_power(
                (white_x, white_y), (target_x, target_y)
            )

            print('====== 수비샷 정보 ======')
            print(f'Current Target: {target_idx}번 공')
            print(f'목표: ({target_x:.2f}, {target_y:.2f})를 직접 조준')
            print(f'계산된 각도: {angle:.2f}도, 파워: {power:.2f}')
            print('====================')

    ##############################
    # 게임 로직 끝
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)
