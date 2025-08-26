# import sys
# sys.stdin = open('sample_input.txt')

def tile(N):
    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 3

    for i in range(3, N+1):
        dp[i] = dp[i-1] + 2*dp[i-2] + dp[i-3]

    return dp[N]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    result = tile(N)
    print(f'#{test_case} {result}')