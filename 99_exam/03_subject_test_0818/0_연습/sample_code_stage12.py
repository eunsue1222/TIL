# https://github.com/khj1259/Spring_Study/blob/master/%EC%9D%BC%ED%83%80%EC%82%AC%ED%94%BC/Sample%20Code/%EC%B5%9C%EC%A2%85%EC%86%8C%EC%8A%A4_stage12_%EA%B9%80%ED%98%84%EC%A0%95.java

import socket
import math

# User and Game Server Information
NICKNAME = '파이썬'
HOST = '127.0.0.1'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [ [0, 0], [130, 0], [260, 0],
          [0, 130], [130, 130], [260, 130] ]

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
        recv_data = (self.sock.recv(1024)).decode()
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
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
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
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def play(conn, gameData):
    angle = 0
    power = 100
    ######################################################################################
    cue_x, cue_y = gameData.balls[0]  # 흰 공 좌표

    # 1~4번 공 중 살아있는 첫 번째 공을 타깃으로 선택
    for target_idx, pwr in [(1, 110), (2, 120), (3, 110), (4, 115)]:
        tx, ty = gameData.balls[target_idx]
        if tx != 0 or ty != 0:  # 좌표가 (0,0)이 아니라면 공이 존재
            dx, dy = tx - cue_x, ty - cue_y
            rad = math.atan2(dy, dx)
            deg = rad * 180 / math.pi
            angle = 90 - deg      # SSAFY 좌표계 변환
            power = pwr
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
