import socket
import math

# User and Game Server Information
NICKNAME = '_파이썬'
HOST = '127.0.0.1'
PORT = 1447  # Do not modify

# predefined variables (Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [[0, 0], [130, 0], [260, 0],
         [0, 130], [130, 130], [260, 130]]


class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
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
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)

    def close(self):
        self.sock.close()


class GameData:
    def __init__(self):
        self.reset()

    def reset(self):
        self.balls = [[0, 0] for _ in range(NUMBER_OF_BALLS)]

    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)

    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' %
                  (i, self.balls[i][0], self.balls[i][1]))
        print()


def play(conn, gameData):
    cue_x, cue_y = gameData.balls[0]  # 흰 공 좌표
    angle = 0
    power = 100

    ######################################################################################
    # 살아있는 공 중 가장 먼저 나오는 공 선택
    for target_idx, base_power in [(1, 130), (2, 115), (3, 105), (4, 115)]:
        tx, ty = gameData.balls[target_idx]
        if tx != 0 or ty != 0:
            # 각 홀까지 거리 계산 후 가장 가까운 포켓 선택
            closest_hole = min(HOLES, key=lambda h: math.hypot(h[0]-tx, h[1]-ty))
            hx, hy = closest_hole

            # 타깃 공 -> 포켓 방향
            offset_x = hx - tx
            offset_y = hy - ty

            # 흰 공 -> 타깃 공까지 벡터
            dx = tx - cue_x - offset_x*0.1 # 공 중심 보정
            dy = ty - cue_y - offset_y*0.1 # 공 중심 보정

            rad = math.atan2(dy, dx)
            deg = rad * 180 / math.pi
            angle = 90 - deg

            # 거리 기반 파워 조절
            distance = math.hypot(dx, dy)
            power = min(max(int(distance*1.2), 80), 150)  # 최소 80, 최대 150
            break
    ######################################################################################
    conn.send(int(angle), int(power))


def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        gameData.show()
        play(conn, gameData)
    conn.close()
    print('Connection Closed')


if __name__ == '__main__':
    main()
