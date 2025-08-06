# import sys
# sys.stdin = open('input.txt', 'r')

from collections import deque

# 방향 벡터: 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    # 큐 생성
    queue = deque()
    queue.append((x, y))

    # 방문 처리
    distance[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N: # 범위 체크
                cost = distance[x][y] + grid[nx][ny] # 다음까지 최소 복구 시간 = 현재까지 최소 복구 시간 + 다음의 최소 복구 시간
                if distance[nx][ny] > cost: # distance[nx][ny]: 해당 칸까지의 최소 복구 시간
                    distance[nx][ny] = cost
                    queue.append((nx, ny))


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input())) for _ in range(N)]

    # 초기화
    distance = [[float('inf')] * N for _ in range(N)] # 최소 복구 시간

    # 시작점
    bfs(0, 0)

    print(f'#{test_case} {distance[N-1][N-1]}')