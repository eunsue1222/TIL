# https://gist.github.com/ManduTheCat/1b23a7ece25ca7c16cf193da63a30c0b

import socket
import math

# User and Game Server Information
NICKNAME = 'PYTHON_PLAYER'
HOST = '127.0.0.1'
PORT = 1447  # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME + '/'
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')

    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')

    def receive(self):
        recv_data = self.sock.recv(1024).decode()
        print('Data Received: ' + recv_data)
        return recv_data

    def send(self, angle, power):
        merged_data = '%d/%d/' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)

    def close(self):
        self.sock.close()


class GameData:
    def __init__(self):
        self.reset()

    def reset(self):
        self.balls = [[-1, -1] for _ in range(NUMBER_OF_BALLS)]

    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = float(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)

    def show(self):
        print('=== Balls Positions ===')
        for i in range(NUMBER_OF_BALLS):
            print(f'Ball {i}: {self.balls[i][0]}, {self.balls[i][1]}')
        print()


def play(conn, gameData, order):
    angle = 0
    power = 100

    whiteBall_x, whiteBall_y = gameData.balls[0]

    # 타겟 공 선택: 선공(1,3,5) / 후공(2,4,5)
    isTarget = [False] * NUMBER_OF_BALLS
    if order == 1:
        for idx in [1, 3, 5]:
            if gameData.balls[idx][0] != -1 and gameData.balls[idx][1] != -1:
                isTarget[idx] = True
                break
    else:
        for idx in [2, 4, 5]:
            if gameData.balls[idx][0] != -1 and gameData.balls[idx][1] != -1:
                isTarget[idx] = True
                break

    # 타겟 공 좌표 결정
    targetBall_x, targetBall_y = -1, -1
    for i in range(1, NUMBER_OF_BALLS):
        if isTarget[i]:
            targetBall_x, targetBall_y = gameData.balls[i]
            break
    if targetBall_x == -1 and targetBall_y == -1:
        targetBall_x, targetBall_y = gameData.balls[5]

    dx = targetBall_x - whiteBall_x
    dy = targetBall_y - whiteBall_y
    width = abs(dx)
    height = abs(dy)

    # 사분면별 각도 계산
    if whiteBall_x == targetBall_x:
        angle = 0 if whiteBall_y < targetBall_y else 180
    elif whiteBall_y == targetBall_y:
        angle = 90 if whiteBall_x < targetBall_x else 270
    else:
        if whiteBall_x < targetBall_x and whiteBall_y < targetBall_y:  # 1사분면
            rad = math.atan(height / width)
            angle = math.degrees(rad)
        elif whiteBall_x > targetBall_x and whiteBall_y < targetBall_y:  # 2사분면
            rad = math.atan(height / width)
            angle = math.degrees(rad) + 270
        elif whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:  # 3사분면
            rad = math.atan(width / height)
            angle = math.degrees(rad) + 180
        elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:  # 4사분면
            rad = math.atan(height / width)
            angle = math.degrees(rad) + 90

    # power 계산 (거리 기반, 기본 100)
    distance = math.hypot(dx, dy)
    power = min(100, distance + 5)

    conn.send(int(angle), int(power))


def main():
    conn = Conn()
    gameData = GameData()
    order = 1  # 기본값, 서버에서 SIGNAL_ORDER로 업데이트 가능

    while True:
        gameData.read(conn)

        # 서버가 선공/후공 신호를 보내면 order 업데이트
        if gameData.balls[0][0] == 9908:
            order = int(gameData.balls[0][1])
            print(f'* You will be the {"first" if order==1 else "second"} player. *\n')
            continue
        elif gameData.balls[0][0] == 9909:  # 종료 신호
            break

        gameData.show()
        play(conn, gameData, order)

    conn.close()
    print('Connection Closed')


if __name__ == '__main__':
    main()
