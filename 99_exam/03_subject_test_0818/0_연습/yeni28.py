# https://github.com/yeni28/yeni28/blob/main/%EC%9D%BC%ED%83%80%EC%8B%B8%ED%94%BC/otehr.py

import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'GWANGJU02_KIMYEAEYN'

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

  # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    # 선공이면 1,3,8 후공이면 2,4,8 순서로 공을 선택한다.
    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    # 선공이면 1,3,8 후공이면 2,4,8 순서로 공을 선택한다.
    if order == 1:
        ball_list = [1,3,5]
    else:
        ball_list = [2,4,5]
    
    for n in ball_list:
        if balls[n][0] > -1 and balls[n][1] > -1:
            targetBall_x = balls[n][0]
            targetBall_y = balls[n][1]
            break

    # 1. 흰색공이 이동해야할 좌표(x,y) 구하기
    r = 5.74/2
    if targetBall_x < whiteBall_x: #흰공이 오른쪽이면
        s = (0 -targetBall_y)/(0-targetBall_x)
        seta = math.atan(s)
        x = targetBall_x - 2 * r * (math.cos(seta))
        y = targetBall_y - 2 * r * (math.sin(seta))

    elif targetBall_x > whiteBall_x: #흰공이 왼쪽이면
        s = (0 - targetBall_y) / (0 + targetBall_x)
        seta = math.atan(s)
        x = targetBall_x - 2 * r * (math.cos(seta))
        y = targetBall_y - 2 * r * (math.sin(seta))

    # 2. 최종적으로 이동해야 할 홀 구하기
    # HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
    max_V = 0 
    target_hole = HOLES[0]
    for i in HOLES:
        a_2 = (i[0]-targetBall_x)**2 + (i[1]-targetBall_y)**2
        b_2 = (targetBall_x-whiteBall_x)**2 + (targetBall_y-whiteBall_y)**2
        c_2 = (i[0]-whiteBall_x)**2 + (i[1]-whiteBall_y)**2
        angle1 = math.acos((a_2 + b_2 - c_2)/(2*((a_2)**(1/2))*((b_2)**(1/2))))
        angle1 = math.degrees(angle1)
        if 90 < angle1 <= 180 and max_V < angle1:
            max_V = angle1
            target_hole = i
    # 3. 그 때 수구를 보내야 할 각도 구하기
        hole_x = target_hole[0]
        hole_y = target_hole[1]

        if x < hole_x and y > hole_y:
            angle = math.atan((hole_x-x)/(y-hole_y))
            angle = math.degrees(angle)
            angle = 360 - angle
        elif x < hole_x and y < hole_y:
            angle = math.atan((hole_x-x)/(hole_y-y))
            angle = math.degrees(angle)
            angle = 180 + angle
        elif x > hole_x and y < hole_y:
            angle = math.atan((x-hole_x)/(hole_y-y))
            angle = math.degrees(angle)
            angle = 180 - angle

        # 4. 수구를 보낼 힘 정하기

        width = abs(hole_x - targetBall_x)
        height = abs(hole_y - targetBall_y)
        distance = math.sqrt(width**2 + height**2)
        power = distance * 0.5
        
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