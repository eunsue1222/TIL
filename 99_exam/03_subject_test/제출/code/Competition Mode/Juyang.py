import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '박주양'

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
qwe = 1


def cal_hole(radian,wh_x,wh_y,sa):
    min_rad = float('inf')

    for emp in range(6):
        emp_wid = abs(wh_x - HOLES[emp][0])
        emp_heg = abs(wh_y - HOLES[emp][1])

        if sa == 3 and wh_x > HOLES[emp][0] and wh_y > HOLES[emp][1]:
            rad = math.atan(emp_wid / emp_heg)
            ang = (180 / math.pi * rad) + 180
            if min(min_rad,abs(radian - ang)) == abs(radian - ang):
                min_rad = abs(radian - ang)
                answer = (ang,HOLES[emp][0],HOLES[emp][1])

        if sa == 4 and wh_x < HOLES[emp][0] and wh_y > HOLES[emp][1]:
            rad = math.atan(emp_wid / emp_heg)
            ang = (180 / math.pi * rad) + 90

            if min(min_rad, abs(radian - ang)) == abs(radian - ang):
                min_rad = abs(radian - ang)
                answer = (ang,HOLES[emp][0],HOLES[emp][1])

        if sa == 2 and wh_x > HOLES[emp][0] and wh_y < HOLES[emp][1]:
            rad = math.atan(emp_wid / emp_heg)
            ang = (180 / math.pi * rad) + 270

            if min(min_rad, abs(radian - ang)) == abs(radian - ang):
                min_rad = abs(radian - ang)
                answer = (ang,HOLES[emp][0],HOLES[emp][1])

        if wh_x < HOLES[emp][0] and wh_y < HOLES[emp][1]:
            rad = math.atan(emp_wid / emp_heg) if emp_heg > 0 else 0
            ang = 180 / math.pi * rad
            if min(min_rad, abs(radian - ang)) == abs(radian - ang):
                min_rad = abs(radian - ang)
                answer = (ang,HOLES[emp][0],HOLES[emp][1])

    return answer


def cal_distance(hole, ori, k=0.3):
    """
    hole : 목적구 -> 홀 각도
    ori  : 흰공 -> 목적구 각도
    k    : 보정 강도 (0~1 사이 값, 0.3~0.5 추천)
    """
    # 각도 차이 구하기
    delta = (hole - ori + 180) % 360 - 180  # -180 ~ +180 범위로 정규화

    # ori에 delta의 일부만 반영
    adjusted_angle = ori + delta * k
    return adjusted_angle


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
    if balls[qwe][0] == float(-1) and balls[qwe][1] == float(-1):
        qwe += 1



    targetBall_x = balls[qwe][0]
    targetBall_y = balls[qwe][1]

    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)

    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    radian = math.atan(width / height) if height > 0 else 0
    angle = 180 / math.pi * radian
    dir= 1
    # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
    if whiteBall_x == targetBall_x:
        if whiteBall_y < targetBall_y:
            angle = 0
        else:
            angle = 180
    elif whiteBall_y == targetBall_y:
        if whiteBall_x < targetBall_x:
            angle = 90
        else:
            angle = 270

    # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
    if whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(width / height)
        print('3사문면 들어옴')
        angle = (180 / math.pi * radian) + 180
        dir = 3

    # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(height / width)
        print('4사문면 들어옴')
        angle = (180 / math.pi * radian) + 90
        dir = 4


    # 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x > targetBall_x and whiteBall_y < targetBall_y:
        print('2사분면들어옴')
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 270
        dir = 2

    hole_dir = cal_hole(angle,whiteBall_x,whiteBall_y,dir)
    print('---------------------------------------------')
    print(f'넣으려는 홀의 라디안 및 위치 : {hole_dir}')
    print('---------------------------------------------')

    emp_dir1 = cal_distance(hole_dir[0],angle)

    # distance: 두 점(좌표) 사이의 거리를 계산
    distance = math.sqrt(width ** 2 + height ** 2)

    # power: 거리 distance에 따른 힘의 세기를 계산
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
    print(f'기존 angle:{angle}')
    print(f'새로운 angle:{emp_dir1}')
    merged_data = '%f/%f/' % (emp_dir1, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')





'''
알고리즘
> 1차적으론 치려는 공의 사분면 판단후 
> 각 홀의 라디안과 지금 치려는 고으이 라디안을 서로 비교함 
> 공의 칠 각도 계산 


cal_hole 함수는 6개의 홀을 각각 각도를 계산하는 함수
radian 매개변수를 통해 치려는 공과의 각도가 가장 작은 홀을 찾고
그 홀 값의 각도와 ,x,y좌표를 리턴함


cal_distance 함수는 치려는 공과 , 치려는 홀의 각도차이를 판별하여
공을 칠때 방향을 조절함 , 
이를 통해 실제 당구와 동일하게 각도를 조절하여 치게됨


'''