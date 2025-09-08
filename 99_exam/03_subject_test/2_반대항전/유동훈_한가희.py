import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '쁘띠동훈'

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

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

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
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # --------------------------------------------------------------------------
    # [게임 설정 및 상수]
    BALL_RADIUS = 2.865  # 공의 반지름
    BALL_DIAMETER = 5.73  # 공의 지름
    # --------------------------------------------------------------------------

    # [전략적 목표 설정]
    # 1. order에 따라 자신의 공(홀수/짝수)을 결정합니다.
    if order == 1:
        my_ball_numbers = [1, 3]
    else:
        my_ball_numbers = [2, 4]

    # 2. 아직 테이블 위에 남아있는 '자신의 공'들을 찾습니다.
    remaining_my_balls = []
    for ball_num in my_ball_numbers:
        # balls 배열에서 해당 번호의 공 좌표를 확인
        if balls[ball_num][0] > 0:
            remaining_my_balls.append(balls[ball_num])

    # 3. 쳐야 할 공이 없으면 5번 공을 목표로 설정
    if not remaining_my_balls:
        if balls[5][0] > 0:
            remaining_my_balls.append(balls[5])

    # --------------------------------------------------------------------------
    # [샷 계산] - 모든 경우의 수를 탐색하여 최적의 샷을 선택

    angle = 0
    power = 0
    best_shot = None
    min_score = float('inf')  # 가장 낮은 난이도 점수를 찾기 위한 초기값

    # 1. 나의 남은 모든 공을 순회
    for target_ball_coords in remaining_my_balls:
        target_x, target_y = target_ball_coords[0], target_ball_coords[1]

        # 2. 6개의 모든 홀을 순회
        for hole in HOLES:

            # [A. 현재 (목표구, 홀) 조합에 대한 샷 정보 계산]
            # 1. 홀에서 목적구를 잇는 방향 벡터 및 거리(magnitude) 계산
            vec_x = target_x - hole[0]
            vec_y = target_y - hole[1]
            dist_target_hole = math.sqrt(vec_x ** 2 + vec_y ** 2)  # 목표구-홀 거리
            unit_vec_x = vec_x / dist_target_hole if dist_target_hole > 0 else 0
            unit_vec_y = vec_y / dist_target_hole if dist_target_hole > 0 else 0

            # 2. 조준점(Aim Point) 계산
            aim_x = target_x + unit_vec_x * BALL_DIAMETER
            aim_y = target_y + unit_vec_y * BALL_DIAMETER

            # 3. 흰 공과 조준점 사이의 거리와 각도 계산
            delta_x = aim_x - whiteBall_x
            delta_y = aim_y - whiteBall_y
            dist_white_aim = math.sqrt(delta_x ** 2 + delta_y ** 2)  # 흰공-조준점 거리

            radian = math.atan2(delta_y, delta_x)
            shot_angle = math.degrees(radian)
            shot_angle = (450 - shot_angle) % 360

            # [B. 현재 샷의 '난이도' 점수 평가]
            dot_product = delta_x * -unit_vec_x + delta_y * -unit_vec_y
            cos_theta = dot_product / (dist_white_aim * 1)
            cos_theta = max(-1.0, min(1.0, cos_theta))
            cut_angle_score = math.degrees(math.acos(cos_theta))

            is_obstructed = False
            obstacle_balls = [b for i, b in enumerate(balls) if i > 0 and b != target_ball_coords]

            for obs in obstacle_balls:
                obs_x, obs_y = obs[0], obs[1]
                if obs_x <= 0: continue

                dist_to_path = abs((aim_y - whiteBall_y) * obs_x - (
                            aim_x - whiteBall_x) * obs_y + aim_x * whiteBall_y - aim_y * whiteBall_x) / dist_white_aim
                dot_p = (obs_x - whiteBall_x) * (aim_x - whiteBall_x) + (obs_y - whiteBall_y) * (aim_y - whiteBall_y)
                if dist_to_path < BALL_DIAMETER and 0 < dot_p < dist_white_aim ** 2:
                    is_obstructed = True
                    break

            obstruction_score = 9999 if is_obstructed else 0

            # [C. 최종 점수 합산 및 최고점 샷 갱신]
            total_score = cut_angle_score + obstruction_score

            if total_score < min_score:
                min_score = total_score
                # 최고점 샷 정보에 '목표구-홀 거리'도 함께 저장
                best_shot = {'angle': shot_angle, 'dist_aim': dist_white_aim, 'dist_hole': dist_target_hole}

    # 3. 모든 계산이 끝난 후, '최고의 샷'으로 결정된 값들을 최종 사용
    if best_shot:
        angle = best_shot['angle']

        # ==================================================================
        # [수정된 부분: 힘 계산 시 두 거리를 모두 고려]
        distance_to_aim = best_shot['dist_aim']
        distance_to_hole = best_shot['dist_hole']

        # 총 이동 거리를 기반으로 힘 계산
        total_distance = distance_to_aim + distance_to_hole

        if total_distance < 1:
            power = total_distance * 5
        elif total_distance > 150:
            power = total_distance * 0.25  # 장거리 힘 계수 소폭 상향
        else:
            power = total_distance * 0.5  # 기본 힘 계수 소폭 상향
        # ==================================================================

    # 최종 힘(power) 값은 100을 넘지 않도록 제한
    if power > 100:
        power = 100
    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')