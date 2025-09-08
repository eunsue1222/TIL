import socket
import math

# User and Game Server Information
NICKNAME = '서울6반_김현정_파이썬'
HOST = '127.0.0.1'
PORT = 1447

# Predefined variables
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [[0,0], [130,0], [260,0], [0,130], [130,130], [260,130]]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect:', HOST, PORT)
        self.sock.connect((HOST, PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')

    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data corrupted, resend requested.')

    def receive(self):
        recv_data = self.sock.recv(1024).decode()
        print('Data Received:', recv_data)
        return recv_data

    def send(self, angle, power):
        merged_data = f'{int(angle)}/{int(power)}'
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent:', merged_data)

    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()

    def reset(self):
        self.balls = [[0,0] for _ in range(NUMBER_OF_BALLS)]

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
        print('=== Balls Positions ===')
        for i, (x, y) in enumerate(self.balls):
            print(f'Ball{i}: {x}, {y}')
        print()

def play(conn, gameData):
    cue_x, cue_y = gameData.balls[0]
    angle = 0
    power = 100

    # 살아있는 공 찾기
    for target_idx, base_power in [(1,130),(2,115),(3,105),(4,115)]:
        tx, ty = gameData.balls[target_idx]
        if tx != 0 or ty != 0:
            # 가장 가까운 포켓 찾기
            hx, hy = min(HOLES, key=lambda h: math.hypot(h[0]-tx, h[1]-ty))

            # 벽 튕김 고려
            dx = tx - cue_x
            dy = ty - cue_y
            # x 범위 체크
            if cue_x + dx < 0 or cue_x + dx > TABLE_WIDTH:
                dx = -dx
            # y 범위 체크
            if cue_y + dy < 0 or cue_y + dy > TABLE_HEIGHT:
                dy = -dy

            # 타깃 공 → 포켓 벡터 조정
            offset_x = hx - tx
            offset_y = hy - ty
            dx -= offset_x*0.1
            dy -= offset_y*0.1

            # 각도 계산
            rad = math.atan2(dy, dx)
            deg = rad * 180 / math.pi
            angle = 90 - deg

            # 거리 기반 파워 최적화
            distance = math.hypot(dx, dy)
            power = min(max(int(distance*1.2), 80), 150)
            break

    conn.send(angle, power)

def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        gameData.show()
        play(conn, gameData)
    conn.close()

if __name__ == '__main__':
    main()
