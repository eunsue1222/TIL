# import sys
# sys.stdin = open('sample_input.txt')

def binomial_coefficient(n, a, b):
    dp = [[0] * (n+1) for _ in range(n+1)]

    if a + b != n:
        return 0

    for i in range(n+1):
        for j in range(a+1):
            if j == 0 or i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    return dp[n][a]


T = int(input())
for test_case in range(1, T+1):
    n, a, b = map(int, input().split())

    result = binomial_coefficient(n, a, b)
    print(f'#{test_case} {result}')