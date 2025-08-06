# import sys
# sys.stdin = open('input.txt', 'r')

from collections import deque

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    # 큐 생성
    queue = deque()
    queue.append((x, y))

    # 방문 처리
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny] and maze[nx][ny] != 1: # 탐색 가능 여부 체크
                if maze[nx][ny] == 3: # 도착점
                    return 1
                queue.append((nx, ny))
                visited[nx][ny] = True
    return 0


T = 10
for _ in range(T):
    test_case = int(input())
    maze = [list(map(int, input())) for _ in range(16)] # 0: 길, 1: 벽, 2: 출발점, 3: 도착점

    # 시작점 찾기
    is_found = False
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                is_found = True
                x, y = i, j
                break
        if is_found:
            break

    # 초기값 설정
    visited = [[False] * 16 for _ in range(16)]

    # 시작점
    is_reached = bfs(x, y)

    print(f'#{test_case} {is_reached}')