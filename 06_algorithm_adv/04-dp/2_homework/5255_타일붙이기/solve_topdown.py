# import sys
# sys.stdin = open('sample_input.txt')

dp = {}

def tile(N):
    if N == 0:
        return 1
    elif N == 1:
        return 1
    elif N == 2:
         return 3

    if N in dp:
        return dp[N]

    dp[N] = tile(N-1) + 2*tile(N-2) + tile(N-3)
    return dp[N]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    result = tile(N)
    print(f'#{test_case} {result}')