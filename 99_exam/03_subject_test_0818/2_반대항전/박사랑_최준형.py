import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '대전4_박사랑_최준형'

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

    print(order)
    # === 틱톡 방지만 위한 최소 추가 ===
    BALL_RADIUS = 2.865  # 공 반지름(지름≈5.73)
    BALL_DIAMETER = BALL_RADIUS * 2


    def nudge_for_tiktok(wx, wy, tx, ty):
        """
        흰공-목적구가 거의 수평 정렬( dy ≈ 0 )이면
        목적구의 '조준점'을 수직 방향으로 반지름 정도 살짝 옮겨
        직선 충돌 반복(틱톡)을 방지.
        (기존 각도/파워 로직은 그대로)
        """
        dx, dy = tx - wx, ty - wy
        dist_wt = math.hypot(dx, dy)
        if dist_wt < 1e-6:
            return tx, ty

        # 수평 정렬 임계: dy가 작고, x로는 충분히 떨어져 있을 때
        if abs(dy) <= BALL_RADIUS * 0.8 and abs(dx) >= BALL_DIAMETER * 1.2:
            # 흰공→타깃 단위벡터와 수직 단위벡터
            ux, uy = dx / dist_wt, dy / dist_wt
            px, py = -uy, ux

            # 방향은 테이블 중앙 기준으로 고정(프레임마다 좌우 뒤바뀜 방지)
            cx = TABLE_WIDTH / 2.0
            sgn = 1.0 if (tx - cx) >= 0 else -1.0

            # 오프셋 크기: 0.5R ~ 1.1R
            k = max(0.5, min(1.1, abs(dx) / 80.0))
            off = BALL_RADIUS * k * sgn

            tx = tx + px * off
            ty = ty + py * off

        return tx, ty


    # === 최소 추가 끝 ===

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # -------- Stage 6 전용: order에 따라 내 공만 타깃 선택 --------
    # -------- order별 내 공 타깃 + 둘 다 빠지면 8번(인덱스 5) --------
    targetBall_x = None
    targetBall_y = None
    min_d = float('inf')

    # 선공(order=1) => 1,3 / 후공(order=2) => 2,4
    candidate_indices = (1, 3) if order == 1 else (2, 4)

    # 내 공 중 테이블 위에 있는 것들 중에서 가장 가까운 공 선택
    for i in candidate_indices:
        x, y = balls[i]
        if x >= 0 and y >= 0:
            d = math.hypot(x - whiteBall_x, y - whiteBall_y)
            if d < min_d:
                min_d = d
                targetBall_x, targetBall_y = x, y

    # 내 공이 둘 다 빠졌다면 8번 공(인덱스 5)으로 전환
    if targetBall_x is None:
        x8, y8 = balls[5]
        if x8 >= 0 and y8 >= 0:
            targetBall_x, targetBall_y = x8, y8
        else:
            # (안전) 8번도 없으면 기존 fallback 유지
            for i in range(1, len(balls)):
                x, y = balls[i]
                if x != -1 and y:
                    targetBall_x, targetBall_y = x, y
                    break



    # >>> 틱톡 방지: 목표점을 살짝 비껴주기(수평 정렬일 때만 적용)
    targetBall_x, targetBall_y = nudge_for_tiktok(whiteBall_x, whiteBall_y, targetBall_x, targetBall_y)

    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)

    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    radian = math.atan(width / height) if height > 0 else 0
    angle = 180 / math.pi * radian

    cnt = 0
    for j in range(1, len(balls)):
        if whiteBall_y == balls[j][1]:
            cnt += 1

    # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
    if whiteBall_x == targetBall_x:
        if whiteBall_y < targetBall_y:
            angle = 0
        else:
            angle = 180
    elif whiteBall_y == targetBall_y:
        if whiteBall_x < targetBall_x:
            if cnt >= 2:  # 공이 연달아 3개 나란히 있는 경우에만 살짝 빗겨치기
                angle = 89.5
            else:
                angle = 90
        else:
            angle = 270

    # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
    if whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(width / height)
        angle = (180 / math.pi * radian) + 180

    # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 90

    # 2사분면 각도 재계산 -> 추가
    elif whiteBall_x > targetBall_x and whiteBall_y < targetBall_y:
        radian = math.atan(height / width)
        # angle = -(180 / math.pi * radian)
        angle = (180 / math.pi * radian) + 270

    # distance: 두 점(좌표) 사이의 거리를 계산
    distance = math.sqrt(width ** 2 + height ** 2)

    # power: 거리 distance에 따른 힘의 세기를 계산
    power = distance * 0.5

    # 거리 너무 가까운데 살살치니까 turn만 소비되는 것 같음
    # 세게치기
    if distance < 80:
        power = distance * 15

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
