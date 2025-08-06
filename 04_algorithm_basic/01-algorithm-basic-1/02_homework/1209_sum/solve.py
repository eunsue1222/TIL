# import sys
# sys.stdin = open('input.txt')

T = 10
for _ in range(T):
    test_case = int(input())
    grid = [list(map(int, input().split())) for _ in range(100)]

    # 초기화
    max_sum = 0
    diagonal1 = 0
    diagonal2 = 0

    for i in range(100):
        row_sum = sum(grid[i]) # 행의 합
        col_sum = sum(grid[j][i] for j in range(100)) # 열의 합
        max_sum = max(max_sum, row_sum, col_sum)

        diagonal1 += grid[i][i] # 대각선의 합
        diagonal2 += grid[i][99-i] # 대각선의 합

    max_sum = max(max_sum, diagonal1, diagonal2) # 최대값

    print(f'#{test_case} {max_sum}')