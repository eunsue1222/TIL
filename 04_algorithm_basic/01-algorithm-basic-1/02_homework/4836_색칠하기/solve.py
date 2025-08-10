# import sys
# sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # N: 칠할 영역의 개수
    board = [[0] * 10 for _ in range(10)] # 10x10 격자

    for _ in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split())) # r1, c1: 왼쪽 위 모서리, r2, c2: 오른쪽 아래 모서리, color: 색깔
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                board[x][y] += color # color=1: 빨강, color=2: 파랑

    result = sum(row.count(3) for row in board) # color=1+2=3: 보라

    print(f'#{test_case} {result}')