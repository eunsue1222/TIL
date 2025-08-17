import socket
import time
import math

# User and Game Server Information
NICKNAME = '파이썬' # 게임에서 사용할 내 닉네임
HOST = '127.0.0.1' # 서버 주소 (로컬에서 실행 중)
PORT = 1447 # 서버 포트 (고정값, 변경 불가) 
# Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254 # 당구대 가로 길이
TABLE_HEIGHT = 124 # 당구대 세로 길이
NUMBER_OF_BALLS = 5 # 게임에서 사용되는 공 개수
HOLES = [ [0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130] ] # 당구대의 6개 포켓 좌표

# 서버 연결: 게임 서버와 통신해서 자기 닉네임을 등록하고, 공 위치 데이터를 받아옵니다.
class Conn:
    # 서버 연결 -> 닉네임 전송
    def __init__(self):
        # 소켓 객체 생성
        self.sock = socket.socket() 
        print('Trying to Connect: ' + HOST + ':' + str(PORT))

        # 서버 연결 시도
        self.sock.connect((HOST, PORT)) 
        print('Connected: ' + HOST + ':' + str(PORT))
        # 내 닉네임 서버에 전송
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')

    # 데이터가 깨졌을 때 재요청
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')

    # 서버에서 오는 데이터 수신 (각 공의 좌표값들)
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    
    # 서버에 샷 결과 전송 (angle / power)
    def send(self, angle, power):
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)

    # 소켓 닫기
    def close(self):
        self.sock.close()


# 게임 데이터 관리: 서버에서 받은 당구공 좌표들을 balls 배열에 저장합니다.
class GameData:
    def __init__(self):
        self.reset()

    # 모든 공 좌표를 (0, 0)으로 초기화
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
        # balls[i] = [x좌표, y좌표]

    # 서버에서 데이터 받아서 balls 배열에 저장
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

    # 현재 모든 공 좌표 출력
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

# 게임 로직: 공 위치를 바탕으로 어떤 각도와 얼마나 세게 칠지를 계산합니다.
# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def play(conn, gameData):
    angle = 0 # 보낼 각도
    power = 0 # 보낼 힘
    ######################################################################################
    BALL_RADIUS = 5.74 / 2

    # 흰 공 좌표
    white_x, white_y = balls[0][0], balls[0][1]

    # 선공/후공에 따른 목적구 후보
    target_candidates = [1, 3, 5] if order == 1 else [2, 4, 5]

    # 아직 살아있는 목적구 찾기
    target_x, target_y = None, None
    for n in target_candidates:
        if balls[n][0] > -1 and balls[n][1] > -1:
            target_x, target_y = balls[n][0], balls[n][1]
            break

    if target_x is None:
        return angle, power  # 칠 공 없음

    # 수구가 맞춰야 할 지점 (목적구 뒤쪽 offset)
    if target_x != white_x:
        slope = (0 - target_y) / (0 - target_x if target_x < white_x else 0 + target_x)
        seta = math.atan(slope)
    else:
        seta = 0

    hit_x = target_x - 2 * BALL_RADIUS * math.cos(seta)
    hit_y = target_y - 2 * BALL_RADIUS * math.sin(seta)

    # 목적구를 넣기 좋은 홀 선택
    max_angle = 0
    target_hole = HOLES[0]
    for hole in HOLES:
        a2 = (hole[0] - target_x) ** 2 + (hole[1] - target_y) ** 2
        b2 = (target_x - white_x) ** 2 + (target_y - white_y) ** 2
        c2 = (hole[0] - white_x) ** 2 + (hole[1] - white_y) ** 2
        try:
            ang = math.acos((a2 + b2 - c2) / (2 * (a2 ** 0.5) * (b2 ** 0.5)))
            ang = math.degrees(ang)
            if 90 < ang <= 180 and ang > max_angle:
                max_angle = ang
                target_hole = hole
        except ValueError:
            continue

    hole_x, hole_y = target_hole

    # 각도 계산
    dx, dy = hole_x - hit_x, hole_y - hit_y
    rad = math.atan2(dy, dx)
    angle = (rad * 180 / math.pi) % 360

    # 힘 계산 (목적구와 홀 거리 기반)
    dist = math.sqrt((hole_x - target_x) ** 2 + (hole_y - target_y) ** 2)
    power = dist * 0.5
    ######################################################################################
    conn.send(angle, power) # 서버에 결과 전송

# 메인 루프: 계속 데이터를 읽고, 보여주고, 내 차례가 되면 샷을 보냅니다.
def main():
    conn = Conn() # 서버 연결
    gameData = GameData() # 게임 데이터 객체 생성
    while True:
        gameData.read(conn) # 서버에서 공 좌표 읽기
        gameData.show() # 공 좌표 출력
        play(conn, gameData) # 샷 계산해서 서버에 angle/power 보내기
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()