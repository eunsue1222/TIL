import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '김안서치현원'

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
BALL_DIAMETER = 5.73

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

# ✨ 새로운 기능: 내 공 그룹을 저장할 변수 (None은 아직 미정 상태)
my_ball_group = None

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

while True:
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

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

    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        my_ball_group = None  # 게임이 새로 시작되면 그룹 초기화
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.

    # 여기서부터 코드를 작성하세요.

    white_ball_pos = balls[0]

    # ✨ 1. 내 공 그룹이 정해졌는지 확인하고, 이번 턴에 칠 공들을 결정합니다.
    # 그룹 1: 1, 3번 공 / 그룹 2: 2, 4번 공
    group_A_indices = [1, 3]
    group_B_indices = [2, 4]

    # 아직 내 그룹이 정해지지 않았다면, 테이블 상태를 보고 판단합니다.
    if my_ball_group is None:
        group_A_on_table = [i for i in group_A_indices if balls[i][0] != -1]
        group_B_on_table = [i for i in group_B_indices if balls[i][0] != -1]

        # 한쪽 그룹의 공이 더 많이 들어가 있다면, 그 반대쪽이 내 그룹입니다.
        if len(group_A_on_table) > len(group_B_on_table):
            my_ball_group = group_A_indices
            print(f"Group Assigned: My balls are {my_ball_group} ( 상대방이 그룹 B 공을 넣음 )")
        elif len(group_B_on_table) > len(group_A_on_table):
            my_ball_group = group_B_indices
            print(f"Group Assigned: My balls are {my_ball_group} ( 상대방이 그룹 A 공을 넣음 )")

    # 이번 턴에 칠 공 리스트 결정
    target_ball_indices = []
    if my_ball_group:
        my_balls_on_table = [i for i in my_ball_group if balls[i][0] != -1]
        if my_balls_on_table:
            target_ball_indices = my_balls_on_table
            print(f"My assigned balls on table: {target_ball_indices}")
        elif balls[5][0] != -1:  # 내 공이 다 없고 8번 공이 있으면 8번 공 타겟
            target_ball_indices = [5]
            print("All my balls are pocketed. Targeting 8-ball.")
    else:  # 아직 그룹이 미정인 '오픈 테이블' 상태
        target_ball_indices = [i for i in [1, 2, 3, 4] if balls[i][0] != -1]
        print("Table is open. Targeting all non-8-balls.")

    # 2. 가능한 모든 샷을 평가하여 최적의 샷 찾기
    best_shot = None
    best_score = -1

    for target_idx in target_ball_indices:
        target_pos = balls[target_idx]

        for hole in HOLES:
            # a. 흰 공이 조준해야 할 가상 지점 계산
            vec_target_to_hole_x = hole[0] - target_pos[0]
            vec_target_to_hole_y = hole[1] - target_pos[1]
            dist_target_to_hole = math.sqrt(vec_target_to_hole_x ** 2 + vec_target_to_hole_y ** 2)
            if dist_target_to_hole == 0: continue

            unit_x = vec_target_to_hole_x / dist_target_to_hole
            unit_y = vec_target_to_hole_y / dist_target_to_hole
            aim_pos_x = target_pos[0] - unit_x * BALL_DIAMETER
            aim_pos_y = target_pos[1] - unit_y * BALL_DIAMETER

            # b. 스크래치 위험도 계산 (흰 공이 포켓에 빠질 위험)
            vec_white_to_aim_x = aim_pos_x - white_ball_pos[0]
            vec_white_to_aim_y = aim_pos_y - white_ball_pos[1]

            dot_product = vec_white_to_aim_x * vec_target_to_hole_x + vec_white_to_aim_y * vec_target_to_hole_y
            mag_white = math.sqrt(vec_white_to_aim_x ** 2 + vec_white_to_aim_y ** 2)
            mag_target = dist_target_to_hole
            if mag_white == 0: continue

            cos_theta = max(-1.0, min(1.0, dot_product / (mag_white * mag_target)))
            angle_between_paths = math.degrees(math.acos(cos_theta))

            # c. 샷 점수 계산
            score = 1000 / (mag_white + mag_target)
            if angle_between_paths < 10:
                score *= (angle_between_paths / 10) ** 2

            if score > best_score:
                best_score = score
                best_shot = {
                    'aim_pos': (aim_pos_x, aim_pos_y),
                    'total_dist': mag_white + mag_target
                }

    # 3. 최종 샷 결정 및 계산
    if best_shot:
        aim_point = best_shot['aim_pos']
        total_distance = best_shot['total_dist']

        dx = aim_point[0] - white_ball_pos[0]
        dy = aim_point[1] - white_ball_pos[1]
        radian = math.atan2(dy, dx)
        angle = (90 - math.degrees(radian) + 360) % 360

        power = total_distance * 0.5
        power = max(power, 15)
        power = min(power, 100)

        print(f"Best shot found! Score: {best_score:.2f}")
    else:
        # 칠 공이 없거나, 모든 샷이 위험해서 걸러진 경우
        print("No good shot found. Playing safe (or passing turn).")
        angle = 0.0
        power = 0.0

    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')
