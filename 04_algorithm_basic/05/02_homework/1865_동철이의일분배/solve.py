def dfs(index, work, percentage):
    

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    possibility = [list(map(int, input().split())) for _ in range(N)]
