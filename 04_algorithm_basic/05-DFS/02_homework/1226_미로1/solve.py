# import sys
# sys.stdin = open('input.txt', 'r')

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global is_reached

    # 종료 조건
    if is_reached == 1:
        return

    # 도착점
    if maze[x][y] == 3:
        is_reached = 1 # 1: 가능함, 0: 가능하지 않음
        return

    # 방문 처리
    visited[x][y] = True

    # 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 16 and 0 <= ny < 16 and maze[nx][ny] != 1 and not visited[nx][ny]: # 탐색 가능 여부 체크
            dfs(nx, ny)

T = 10
for _ in range(T):
    test_case = int(input())
    maze = [list(map(int, input())) for _ in range(16)] # 0: 길, 1: 벽, 2: 출발점, 3: 도착점

    # 시작점 찾기
    is_found = False
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                x, y = i, j
                is_found = True
                break
        if is_found:
            break

    # 초기값 설정
    is_reached = 0
    visited = [[False] * 16 for _ in range(16)]

    # 시작점
    dfs(x, y)

    print(f'#{test_case} {is_reached}')