# https://github.com/khj1259/Spring_Study/blob/master/%EC%9D%BC%ED%83%80%EC%82%AC%ED%94%BC/Sample%20Code/%EC%B5%9C%EC%A2%85%EC%86%8C%EC%8A%A4_stage12_%EA%B9%80%ED%98%84%EC%A0%95.java

import socket
import math

# User and Game Server Information
NICKNAME = "파이썬"
HOST = "127.0.0.1"
PORT = 1447  # Do not modify

# predefined variables (Do not modify)
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [[0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130]]

def main():
    sock = socket.socket()
    print("Trying Connect:", HOST, PORT)
    sock.connect((HOST, PORT))
    print("Connected:", HOST, PORT)

    # Input / Output stream (Python에서는 send/recv 사용)
    send_data = "9901/" + NICKNAME
    sock.send(send_data.encode("utf-8"))
    print("Ready to play.")

    while True:
        # 서버에서 데이터 수신
        recv_data = sock.recv(1024).decode("utf-8")
        print("Data Received:", recv_data)

        # 공 좌표 parsing
        split_data = recv_data.split("/")
        balls = [[0, 0] for _ in range(NUMBER_OF_BALLS)]
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            # 데이터 손상 시 재요청
            sock.send("9902/9902".encode("utf-8"))
            print("Received Data has been currupted, Resend Requested.")
            continue

        # 초기값
        angle = 0
        power = 110
        dx, dy = 0, 0

        # 1번 공이 있으면 → 그 공 목표
        if balls[1][0] != 0 and balls[1][1] != 0:
            power = 110
            dx = balls[1][0] - balls[0][0]
            dy = balls[1][1] - balls[0][1]

        # 없으면 2번 공 목표
        elif balls[2][0] != 0 and balls[2][1] != 0:
            power = 120
            dx = balls[2][0] - balls[0][0]
            dy = balls[2][1] - balls[0][1]

        # 없으면 3번 공 목표
        elif balls[3][0] != 0 and balls[3][1] != 0:
            power = 110
            dx = balls[3][0] - balls[0][0]
            dy = balls[3][1] - balls[0][1]

        # 없으면 4번 공 목표
        elif balls[4][0] != 0 and balls[4][1] != 0:
            power = 115
            dx = balls[4][0] - balls[0][0]
            dy = balls[4][1] - balls[0][1]

        # 각도 계산 (atan2 결과는 라디안 → 도 단위 변환)
        if dx != 0 or dy != 0:
            radian = math.atan2(dy, dx)
            degree = radian * 180 / math.pi
            angle = 90 - degree

        # 결과 전송
        merged_data = f"{int(angle)}/{int(power)}"
        sock.send(merged_data.encode("utf-8"))
        print("Data Sent:", merged_data)

    sock.close()
    print("Connection Closed")

if __name__ == "__main__":
    main()
