import sys
sys.stdin = open('input.txt')

# 방향 벡터: 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(row, col, acc):
    global min_count

    # 가지 치기
    if acc >= min_count:
        return

    # 종료 조건
    if row == N-1 and col == M-1: # 도착점
        min_count = min(min_count, acc)
        return

    # 탐색
    for k in range(4):
        nx = row + dx[k]
        ny = col + dy[k]
        if nx < 0 or nx >= N or ny < 0 or ny >= M: # 범위 확인
            continue
        if visited[nx][ny]: # 방문 여부 확인
            continue
        if not road[nx][ny]: # 길 여부 확인
            continue
        visited[nx][ny] = 1 # 방문 처리
        dfs(nx, ny, acc+1) # 이동
        visited[nx][ny] = 0 # 백트래킹: 방문 처리


# 입력 처리
N, M = map(int, input().split())
road = [list(map(int, input())) for _ in range(N)]

# 방문 배열 및 최소 이동 횟수 초기화
visited = [[False] * M for _ in range(N)]
min_count = float('inf')

# 시작점 방문처리 후 탐색 시작
visited[0][0] = True
dfs(0, 0, 0)

print(min_count)  # 결과 출력