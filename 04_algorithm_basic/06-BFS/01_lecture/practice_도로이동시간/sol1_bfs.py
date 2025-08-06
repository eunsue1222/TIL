import sys
sys.stdin = open('input.txt')

from collections import deque

# 방향 벡터: 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_road_move_time(row, col):
    queue = deque()
    queue.append((0, 0))
    distance[0][0] = 0 # 시작점

    while queue:
        row, col = queue.popleft()
        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]
            if 0 <= nx < N and 0 <= ny < M and distance[nx][ny] == -1 and data[nx][ny]: # 이동 가능 여부 체크
                queue.append((nx, ny))
                distance[nx][ny] = distance[row][col] + 1
                if nx == N-1 and ny == M-1:
                    return # 도착점 도착 가능
    return -1 # 도착점 도착 불가능

# 데이터 입력
N, M = map(int, input().split()) # N: row, M: col
data = [list(map(int, input())) for _ in range(N)]

# 방문 표시
distance = [[-1] * M for _ in range(N)] # 해당 위치까지 걸린 거리

get_road_move_time(0, 0) # 시작점: (0, 0)
print(distance[N-1][M-1])
for dis in distance:
    print(*dis)