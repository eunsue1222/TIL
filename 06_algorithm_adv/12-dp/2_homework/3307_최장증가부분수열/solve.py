# import sys
# sys.stdin = open('sample_input.txt')

def LIS(N, numbers):
    dp = [1] * N

    for i in range(N):
        for j in range(i):
            if numbers[j] < numbers[i]:
                dp[i] = max(dp[j]+1, dp[i])

    return max(dp)


T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # N: 수열의 길이 (1≤N≤1,000)
    numbers = list(map(int, input().split()))

    result = LIS(N, numbers)
    print(f'#{test_case} {result}')