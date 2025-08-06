import sys
sys.stdin = open('input.txt')

from collections import deque

# 방향 벡터: 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_road_move_time(road, N, M):
    queue = deque()
    queue.append((0, 0, 0)) # (x, y, distance)

    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1 # 시작점 방문 처리

    while queue:
        row, col, dist = queue.popleft()
        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: # 범위 확인
                continue
            if visited[nx][ny]: # 방문 여부 확인
                continue
            if road[nx][ny] == 0: # 길 여부 확인
                continue
            if nx == N-1 and ny == M-1: # 도착점
                return dist + 1 # 도착점 도착 가능
            visited[nx][ny] = 1 # 방문 처리
            queue.append((nx, ny, dist+1)) # 다음
    return -1 # 도착점 도착 불가능


# 도로의 크기 N * M 입력 받기
N, M = map(int, input().split())
road = [list(map(int, input())) for _ in range(N)]
result = get_road_move_time(road, N, M)
print(result)