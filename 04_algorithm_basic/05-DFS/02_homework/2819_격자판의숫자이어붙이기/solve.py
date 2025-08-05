# import sys
# sys.stdin = open('sample_input.txt', 'r')

def dfs(depth, x, y, result):
    # 7자리 숫자 만들기
    if depth == 7:
        count.add(result)
        return

    # 동서남북 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(depth+1, nx, ny, result+str(grid[nx][ny]))


T = int(input())
for test_case in range(1, T+1):
    grid = [list(map(int, input().split())) for _ in range(4)]

    count = set()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 시작점
    for row in range(4):
        for col in range(4):
            dfs(0, row, col, '')

    print(f'#{test_case} {len(count)}')