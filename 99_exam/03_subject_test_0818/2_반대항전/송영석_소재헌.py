import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '대전4_송영석_소재헌'

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

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    # 1번공, 3번공, 5번공을 순서대로 불러온다.
    counter = 0
    if order == 1:
        target_balls = [3, 1, 5]
    else:
        target_balls = [4, 2, 5]
    targetBall_x = -1
    targetBall_y = -1
    while targetBall_x == -1 and targetBall_y == -1:
        targetBall_x = balls[target_balls[counter]][0]
        targetBall_y = balls[target_balls[counter]][1]
        counter += 1

    # holes: 구멍의 위치들 모음
    # 구멍에 넣기 가장 쉬운 위치를 찾는다.
    holes = [[0,0], [127,0], [254,0], [0,127], [127,127], [254, 127]]
    x_diff = targetBall_x - whiteBall_x
    y_diff = targetBall_y - whiteBall_y
    radian = math.atan2(y_diff, x_diff)
    angle = 180 / math.pi * radian

    # 구멍에 넣기 가장 쉬운 위치를 찾는다.
    # 구멍에 넣기 가장 쉬운 위치는 충돌 후 각도가 가장 안 벌어지는 각도로 가정하였다.
    target_angle = 360
    target_hole = [0,0]
    for i, j in holes:
        rad = math.atan2(j - targetBall_y, i - targetBall_x)
        ang = 180 / math.pi * rad
        if abs(ang - angle) < target_angle:
            target_hole = [i, j]
            target_angle = abs(ang - angle)

    if target_angle > 45:
        r = 5.73
        single_bounce = [[0,-127+r],[127,-127+r],[254,-127+r],[0,254-r],[127,254-r],[254,254-r],[508-r,0],[508-r,127], [-254+r,0], [-254+r,127]]
        for i, j in single_bounce:
            rad = math.atan2(j - targetBall_y, i - targetBall_x)
            ang = 180 / math.pi * rad
            if abs(ang - angle) < target_angle:
                target_hole = [i, j]
                target_angle = abs(ang - angle)

    # 목적구가 충돌해야 할 위치를 찾는다.
    # 목적구가 가야 하는 방향 벡터를 구해서, 그에서 정확히 180도 반대 방향으로 공의 지름(5.73)만큼 반대 방향에 있는 위치를 구한다.
    target_x_diff = target_hole[0] - targetBall_x
    target_y_diff = target_hole[1] - targetBall_y
    diff_distance = math.sqrt((target_x_diff**2) + (target_y_diff**2))
    target_x = targetBall_x - (target_x_diff * 5.726 / diff_distance)
    target_y = targetBall_y - (target_y_diff * 5.726 / diff_distance)

    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    # target과 x 사이의 각도를 구하면 목적구가 진행해야 하는 방향을 구할 수 있다.

    x_diff = target_x - whiteBall_x
    y_diff = target_y - whiteBall_y
    radian = math.atan2(x_diff, y_diff)
    angle = 180 / math.pi * radian
    if angle < 0:
        angle += 360
    
    # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
    if whiteBall_x == target_x:
        if whiteBall_y < target_y:
            angle = 0
        else:
            angle = 180
    elif whiteBall_y == target_y:
        if whiteBall_x < target_x:
            angle = 90
        else:
            angle = 270

    # d1: 백색 공이 움직여야 하는 거리
    # d2: 목적구가 움직여야 하는 거리
    # target_angle: 충돌 후 목적구가 원래 백색 공의 움직이는 각도에 비해 빗겨가는 각도임.
    d1 = math.sqrt((x_diff**2) + (y_diff**2))
    d2 = math.sqrt((target_x_diff**2) + (target_y_diff**2))

    # power: 거리 d1, d2에 따른 힘의 세기를 계산
    # 최종 이동 거리는 다음 수식의 값에 비례한다.
    power = math.sqrt(d1 + (d2 / (math.cos(target_angle)**2)))

    # 계수 계산
    power *= 2.4


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