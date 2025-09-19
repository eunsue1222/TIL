import socket
import math

NICKNAME = '서울6반_김현정_파이썬'
HOST = '127.0.0.1'
PORT = 1447

TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [[0,0],[130,0],[260,0],[0,130],[130,130],[260,130]]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect:', HOST, PORT)
        self.sock.connect((HOST, PORT))
        self.sock.send(f'9901/{NICKNAME}'.encode())
        print('Ready to play.\n--------------------')

    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data corrupted, resend requested.')

    def receive(self):
        recv_data = self.sock.recv(1024).decode()
        print('Data Received:', recv_data)
        return recv_data

    def send(self, angle, power):
        self.sock.send(f'{int(angle)}/{int(power)}'.encode())
        print('Data Sent:', f'{int(angle)}/{int(power)}')

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
            print(f'Ball{i}: {x},{y}')
        print()

def reflect_position(x, y):
    """벽에 맞으면 반사 좌표 계산"""
    if x < 0: x = -x
    if x > TABLE_WIDTH: x = 2*TABLE_WIDTH - x
    if y < 0: y = -y
    if y > TABLE_HEIGHT: y = 2*TABLE_HEIGHT - y
    return x, y

def play(conn, gameData):
    cue_x, cue_y = gameData.balls[0]
    angle = 0
    power = 100

    best_score = -1
    best_dx, best_dy = 0,0

    for target_idx, base_power in [(1,130),(2,115),(3,105),(4,115)]:
        tx, ty = gameData.balls[target_idx]
        if tx == 0 and ty == 0:
            continue

        # 가장 가까운 포켓 선택
        hx, hy = min(HOLES, key=lambda h: math.hypot(h[0]-tx, h[1]-ty))

        dx = tx - cue_x
        dy = ty - cue_y

        # 1회 벽 반사 시뮬레이션
        rx, ry = reflect_position(cue_x + dx, cue_y + dy)
        dx = rx - cue_x
        dy = ry - cue_y

        # 타깃 공 → 포켓
        offset_x = hx - tx
        offset_y = hy - ty

        # 단순 성공 확률 계산 (거리 기반)
        distance_cue_to_target = math.hypot(dx, dy)
        distance_target_to_hole = math.hypot(offset_x, offset_y)
        score = distance_target_to_hole / distance_cue_to_target if distance_cue_to_target>0 else 0

        if score > best_score:
            best_score = score
            best_dx = dx
            best_dy = dy
            power = min(max(int((distance_cue_to_target + distance_target_to_hole)*1.2), 80), 150)

    rad = math.atan2(best_dy, best_dx)
    deg = rad * 180 / math.pi
    angle = 90 - deg

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
