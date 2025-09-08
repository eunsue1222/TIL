import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'B0006_1434633'

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


def get_distance_angle(whiteball, targetball, hole, r):
    w_x, w_y = whiteball
    t_x, t_y = targetball
    h_x, h_y = hole

      # 1) 목적구 -> 홀 방향 단위벡터
    vx, vy = h_x - t_x, h_y - t_y
    b = math.hypot(vx, vy)
    if b == 0:
        raise ValueError("ball is already in hole.")
    ux, uy = vx / b, vy / b

    # 2) 고스트볼 좌표 = 목적구 - 2r * 방향벡터
    g_x = t_x - 1.0 * r * ux
    g_y = t_y - 1.0 * r * uy

    # 3) 내 공 -> 고스트볼 벡터
    dx, dy = g_x - w_x, g_y - w_y
    if dx == 0 and dy == 0:
        return 0.0

    # 4) atan2로 +x축 기준 CCW 각도를 구하고,
    #    12시(위쪽) 기준 시계 방향 각도로 변환
    theta_x = math.degrees(math.atan2(dy, dx))   # +x축 기준 CCW
    angle = (90.0 - theta_x) % 360.0             # 변환

    return angle


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






    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # targetBall_x = balls[1][0]
    # targetBall_y = balls[1][1]

    # 가장 HOLE에 가까운 공부터 target
    tb_idx = 0
    th_idx = 0
    dist = 381
    
    black_ball = True

    for x in range(1, len(balls)-1):
        if balls[x][0] != -1.0:
            black_ball = False
            for y in range(6):
                x_delta = abs(balls[x][0] - HOLES[y][0])
                y_delta = abs(balls[x][1] - HOLES[y][1])
                temp_dist= x_delta + y_delta
                if dist > temp_dist and temp_dist != 2.0:
                    dist = min(dist, temp_dist)
                    tb_idx = x
                    th_idx = y
    if black_ball == True:
        targetBall_x = balls[5][0]
        targetBall_y = balls[5][1]
    else:
        targetBall_x = balls[tb_idx][0]
        targetBall_y = balls[tb_idx][1]


    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)

    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    radian = math.atan(width / height) if height > 0 else 0
    angle = 180 / math.pi * radian
    

    # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
    # 일직선상에 있어도 직선으로 쏴 넣을 확률은 1/30000
    if whiteBall_x == targetBall_x:
        if whiteBall_y < targetBall_y:
#            angle = 0
            angle = 2
        else:
#            angle = 180
            angle = 182
    elif whiteBall_y == targetBall_y:
        if whiteBall_x < targetBall_x:
#            angle = 90
            angle = 92
        else:
#            angle = 270
            angle = 272


    

    # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
    if whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(width / height)
        angle = (180 / math.pi * radian) + 180

    
    # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 90


    # My code (2사분면)
    elif whiteBall_x > targetBall_x and whiteBall_y < targetBall_y:
        radian = math.atan(width / height)
#        angle = (180 / math.pi * radian) + 180 + 2*(90 - (180 / math.pi * radian))
        angle = 269 + (90 - (180 / math.pi * radian))

    print(f"targetball_x: {targetBall_x}, targetball_y: {targetBall_y}, angle: {angle}")

    # distance: 두 점(좌표) 사이의 거리를 계산
    distance = math.sqrt(width**2 + height**2)

    # power: 거리 distance에 따른 힘의 세기를 계산
    if distance < 10:
        power = 50
    power = distance * 0.5



            # targetBall_x, targetBall_y: 1번 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    targetBall_x = balls[1][0]
    targetBall_y = balls[1][1]

    # targetBall_x, targetBall_y: 2번 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    targetBall2_x = balls[2][0]
    targetBall2_y = balls[2][1]

    # targetBall_x, targetBall_y: 3번 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    targetBall3_x = balls[3][0]
    targetBall3_y = balls[3][1]

    # targetBall_x, targetBall_y: 4번 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    targetBall4_x = balls[4][0]
    targetBall4_y = balls[4][1]

    # targetBall_x, targetBall_y: 5번 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    targetBall5_x = balls[5][0]
    targetBall5_y = balls[5][1]

    # width, height: 1번 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)

    # width, height: 2번 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width2 = abs(targetBall2_x - whiteBall_x)
    height2 = abs(targetBall2_y - whiteBall_y)

    # width, height: 3번 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width3 = abs(targetBall3_x - whiteBall_x)
    height3 = abs(targetBall3_y - whiteBall_y)

    # width, height: 4번 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width4 = abs(targetBall4_x - whiteBall_x)
    height4 = abs(targetBall4_y - whiteBall_y)

    # width, height: 5번 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width5 = abs(targetBall5_x - whiteBall_x)
    height5 = abs(targetBall5_y - whiteBall_y)

    # distance: 두 점(좌표) 사이의 거리를 계산
    distance1 = math.sqrt(width ** 2 + height ** 2)
    distance2 = math.sqrt(width2 ** 2 + height2 ** 2)
    distance3 = math.sqrt(width3 ** 2 + height3 ** 2)
    distance4 = math.sqrt(width4 ** 2 + height4 ** 2)
    distance5 = math.sqrt(width5 ** 2 + height5 ** 2)

    if order == 1:
        if 0 < targetBall_x < 254 and 0 < targetBall_y < 127:
            pass
        else:
            distance1 = 30000

        if 0 < targetBall3_x < 254 and 0 < targetBall3_y < 127:
            pass
        else:
            distance3 = 30000

            if whiteBall_x == targetBall5_x:
                if whiteBall_y < targetBall5_y:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 127
                    py = 127
                    angle = 0
                else:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 127
                    py = 127
                    angle = 180
            elif whiteBall_y == targetBall5_y:
                if whiteBall_x < targetBall5_x:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 127
                    py = 127
                    angle = 90
                else:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 127
                    py = 127
                    angle = 270

            # 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
            if whiteBall_x > targetBall5_x and whiteBall_y < targetBall5_y:
                
                # 목적구가 중앙 상단
                if targetBall5_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 127
                    py = 127

                # 목적구가 좌측 상단
                else:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 0
                    py = 127
                print('3 - 2사분면')

            # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x > targetBall5_x and whiteBall_y > targetBall5_y:
                # 목적구가 우측 하단
                if targetBall5_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 0
                    py = 127

                # 목적구가 좌측 하단
                elif targetBall5_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 0
                    py = 0
                print('3 - 3사분면')

            # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x < targetBall5_x and whiteBall_y > targetBall5_y:
                # 목적구가 우측 하단
                if targetBall5_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 0
                    py = 254

                # 목적구가 중앙 하단
                elif targetBall5_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 0
                    py = 127
                print('3 - 4사분면')

            # 목적구가 흰 공을 중심으로 1사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x <= targetBall5_x and whiteBall_y <= targetBall5_y:
                # 목적구가 우측 상단
                if targetBall5_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 254
                    py = 127

                # 목적구가 중앙 상단
                elif targetBall5_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 127
                    py = 127
                print('3 - 1사분면')

            distance = distance5


        # 가까운거 먼저
        if distance1 <= distance3:

            if whiteBall_x == targetBall_x:
                if whiteBall_y < targetBall_y:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall_x
                    ty = targetBall_y
                    px = 127
                    py = 127
                    angle = 0
                else:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall_x
                    ty = targetBall_y
                    px = 127
                    py = 127
                    angle = 180
            elif whiteBall_y == targetBall_y:
                if whiteBall_x < targetBall_x:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall_x
                    ty = targetBall_y
                    px = 127
                    py = 127
                    angle = 90
                else:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall_x
                    ty = targetBall_y
                    px = 127
                    py = 127
                    angle = 270
            # 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
            if whiteBall_x > targetBall_x and whiteBall_y < targetBall_y:

                # 목적구가 우측 상단 (가운데 상단 포켓)
                if targetBall_x >= 127:

                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall_x
                    ty = targetBall_y
                    px = 127
                    py = 127

                # 목적구가 좌측 상단 (좌측 상단 포켓)
                elif targetBall_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall_x
                    ty = targetBall_y
                    px = 0
                    py = 127

                print('2사분면')

            # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
                # 목적구가 우측 하단 (가운데 하단 포켓)
                if targetBall_x >= 127:

                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall_x
                    ty = targetBall_y
                    px = 0
                    py = 127

                # 목적구가 좌측 하단 (좌측 하단 포켓)
                elif targetBall_x < 127:

                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall_x
                    ty = targetBall_y
                    px = 0
                    py = 0

                print('3사분면')

            # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
                # 목적구가 우측 하단
                if targetBall_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall_x
                    ty = targetBall_y
                    px = 0
                    py = 254

                # 목적구가 중앙 하단
                elif targetBall_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall_x
                    ty = targetBall_y
                    px = 0
                    py = 127
                print('4사분면')

            # 목적구가 흰 공을 중심으로 1사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x < targetBall_x and whiteBall_y < targetBall_y:
                # 목적구가 우측 상단
                if targetBall_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall_x
                    ty = targetBall_y
                    px = 254
                    py = 127

                # 목적구가 중앙 상단
                elif targetBall_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall_x
                    ty = targetBall_y
                    px = 127
                    py = 127
                print('1사분면')

            distance = distance1

        else:
            if whiteBall_x == targetBall3_x:
                if whiteBall_y < targetBall3_y:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall3_x
                    ty = targetBall3_y
                    px = 127
                    py = 127
                    angle = 0
                else:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall3_x
                    ty = targetBall3_y
                    px = 127
                    py = 127
                    angle = 180
            elif whiteBall_y == targetBall3_y:
                if whiteBall_x < targetBall3_x:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall3_x
                    ty = targetBall3_y
                    px = 127
                    py = 127
                    angle = 90
                else:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall3_x
                    ty = targetBall3_y
                    px = 127
                    py = 127
                    angle = 270
            # 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
            if whiteBall_x > targetBall3_x and whiteBall_y < targetBall3_y:

                # 목적구가 중앙 상단
                if targetBall3_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall3_x
                    ty = targetBall3_y
                    px = 127
                    py = 127

                # 목적구가 좌측 상단
                elif targetBall3_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall3_x
                    ty = targetBall3_y
                    px = 0
                    py = 127
                print('3 - 2사분면')

            # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x > targetBall3_x and whiteBall_y > targetBall3_y:
                # 목적구가 우측 하단
                if targetBall3_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall3_x
                    ty = targetBall3_y
                    px = 0
                    py = 127

                # 목적구가 좌측 하단
                elif targetBall3_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall3_x
                    ty = targetBall3_y
                    px = 0
                    py = 0
                print('3 - 3사분면')

            # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x < targetBall3_x and whiteBall_y > targetBall3_y:
                # 목적구가 우측 하단
                if targetBall3_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall3_x
                    ty = targetBall3_y
                    px = 0
                    py = 254

                # 목적구가 중앙 하단
                elif targetBall3_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall3_x
                    ty = targetBall3_y
                    px = 0
                    py = 127
                print('3 - 4사분면')

            # 목적구가 흰 공을 중심으로 1사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x <= targetBall3_x and whiteBall_y <= targetBall3_y:
                # 목적구가 우측 상단
                if targetBall3_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall3_x
                    ty = targetBall3_y
                    px = 254
                    py = 127

                # 목적구가 중앙 상단
                elif targetBall3_x < 127:

                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall3_x
                    ty = targetBall3_y
                    px = 127
                    py = 127
                print('3 - 1사분면')

                distance = distance3



    # order is second
    else:
        if 0 < targetBall2_x < 254 and 0 < targetBall2_y < 127:
            pass
        else:
            distance2 = 30000

        if 0 < targetBall4_x < 254 and 0 < targetBall4_y < 127:
            pass
        else:
            distance4 = 30000

            if whiteBall_x == targetBall5_x:
                if whiteBall_y < targetBall5_y:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 127
                    py = 127
                    angle = 0
                else:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 127
                    py = 127
                    angle = 180
            elif whiteBall_y == targetBall5_y:
                if whiteBall_x < targetBall5_x:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 127
                    py = 127
                    angle = 90
                else:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 127
                    py = 127
                    angle = 270
               

            # 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
            if whiteBall_x > targetBall5_x and whiteBall_y < targetBall5_y:

                # 목적구가 중앙 상단
                if targetBall5_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 127
                    py = 127

                # 목적구가 좌측 상단
                elif targetBall5_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 0
                    py = 127
                print('5 - 2사분면')

            # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x > targetBall5_x and whiteBall_y > targetBall5_y:
                # 목적구가 우측 하단
                if targetBall5_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 0
                    py = 127

                # 목적구가 좌측 하단
                elif targetBall5_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 0
                    py = 0
                print('5 - 3사분면')

            # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x < targetBall5_x and whiteBall_y > targetBall5_y:
                # 목적구가 우측 하단
                if targetBall5_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 0
                    py = 254

                # 목적구가 중앙 하단
                elif targetBall5_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 0
                    py = 127
                print('5 - 4사분면')

            # 목적구가 흰 공을 중심으로 1사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x <= targetBall5_x and whiteBall_y <= targetBall5_y:
                # 목적구가 우측 상단
                if targetBall5_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 254
                    py = 127

                # 목적구가 중앙 상단
                elif targetBall5_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall5_x
                    ty = targetBall5_y
                    px = 127
                    py = 127
                print('5 - 1사분면')

            distance = distance5



        # 가까운거 먼저
        if distance2 <= distance4:

            if whiteBall_x == targetBall2_x:
                if whiteBall_y < targetBall2_y:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall2_x
                    ty = targetBall2_y
                    px = 127
                    py = 127
                    angle = 0
                else:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall2_x
                    ty = targetBall2_y
                    px = 127
                    py = 127
                    angle = 180
            elif whiteBall_y == targetBall2_y:
                if whiteBall_x < targetBall2_x:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall2_x
                    ty = targetBall2_y
                    px = 127
                    py = 127
                    angle = 90
                else:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall2_x
                    ty = targetBall2_y
                    px = 127
                    py = 127
                    angle = 270

            # 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
            if whiteBall_x > targetBall2_x and whiteBall_y < targetBall2_y:

                # 목적구가 우측 상단 (가운데 상단 포켓)
                if targetBall2_x >= 127:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall2_x
                    ty = targetBall2_y
                    px = 127
                    py = 127

                # 목적구가 좌측 상단 (좌측 상단 포켓)
                elif targetBall2_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall2_x
                    ty = targetBall2_y
                    px = 0
                    py = 127

                print('2사분면')

            # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x > targetBall2_x and whiteBall_y > targetBall2_y:

                # 목적구가 우측 하단 (가운데 하단 포켓)
                if targetBall2_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall2_x
                    ty = targetBall2_y
                    px = 0
                    py = 127

                # 목적구가 좌측 하단 (좌측 하단 포켓)
                elif targetBall2_x < 127:

                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall2_x
                    ty = targetBall2_y
                    px = 0
                    py = 0

                print('3사분면')

            # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x < targetBall2_x and whiteBall_y > targetBall2_y:

                # 목적구가 우측 하단
                if targetBall2_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall2_x
                    ty = targetBall2_y
                    px = 0
                    py = 254

                # 목적구가 중앙 하단
                elif targetBall2_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall2_x
                    ty = targetBall2_y
                    px = 0
                    py = 127
                print('4사분면')

            # 목적구가 흰 공을 중심으로 1사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x < targetBall2_x and whiteBall_y < targetBall2_y:
                # 목적구가 우측 상단
                if targetBall2_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall2_x
                    ty = targetBall2_y
                    px = 254
                    py = 127

                # 목적구가 중앙 상단
                elif targetBall2_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall2_x
                    ty = targetBall2_y
                    px = 127
                    py = 127
                print('1사분면')

            distance = distance2

        # target is number 4
        else:

            if whiteBall_x == targetBall4_x:
                if whiteBall_y < targetBall4_y:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall4_x
                    ty = targetBall4_y
                    px = 127
                    py = 127
                    angle = 0
                else:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall4_x
                    ty = targetBall4_y
                    px = 127
                    py = 127
                    angle = 180
            elif whiteBall_y == targetBall4_y:
                if whiteBall_x < targetBall4_x:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall4_x
                    ty = targetBall4_y
                    px = 127
                    py = 127
                    angle = 90
                else:
                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall4_x
                    ty = targetBall4_y
                    px = 127
                    py = 127
                    angle = 270
            # 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
            if whiteBall_x > targetBall4_x and whiteBall_y < targetBall4_y:

                # 목적구가 중앙 상단
                if targetBall4_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall4_x
                    ty = targetBall4_y
                    px = 127
                    py = 127

                # 목적구가 좌측 상단
                elif targetBall4_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall4_x
                    ty = targetBall4_y
                    px = 0
                    py = 127
                print('4 - 2사분면')

            # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x > targetBall4_x and whiteBall_y > targetBall4_y:
                # 목적구가 우측 하단
                if targetBall4_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall4_x
                    ty = targetBall4_y
                    px = 0
                    py = 127

                # 목적구가 좌측 하단
                elif targetBall4_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall4_x
                    ty = targetBall4_y
                    px = 0
                    py = 0
                print('4 - 3사분면')

            # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x < targetBall4_x and whiteBall_y > targetBall4_y:
                # 목적구가 우측 하단
                if targetBall4_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall4_x
                    ty = targetBall4_y
                    px = 0
                    py = 254

                # 목적구가 중앙 하단
                elif targetBall4_x < 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall4_x
                    ty = targetBall4_y
                    px = 0
                    py = 127
                print('4 - 4사분면')

            # 목적구가 흰 공을 중심으로 1사분면에 위치했을 때 각도를 재계산
            elif whiteBall_x <= targetBall4_x and whiteBall_y <= targetBall4_y:
                # 목적구가 우측 상단
                if targetBall4_x >= 127:


                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall4_x
                    ty = targetBall4_y
                    px = 254
                    py = 127

                # 목적구가 중앙 상단
                elif targetBall4_x < 127:

                    wx = whiteBall_x
                    wy = whiteBall_y
                    tx = targetBall4_x
                    ty = targetBall4_y
                    px = 127
                    py = 127
                print('4 - 1사분면')

                distance = distance4    


    radius = 5.73 
#    angle = get_distance_angle((whiteBall_x, whiteBall_y), (targetBall_x, targetBall_y), (HOLES[1]), radius)
    angle = get_distance_angle((wx, wy), (tx, ty), (px, py), radius)
#    radians = get_distance_angles((wx, wy), (tx, ty), (px, py), radius)
    
#    angle = math.degrees(radians)

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