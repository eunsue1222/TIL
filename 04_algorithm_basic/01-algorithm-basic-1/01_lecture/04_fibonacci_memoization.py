def fibonacci_memoization(n):
    if n >= 2 and memo[n] == 0:
        memo[n] = fibonacci_memoization(n-1) + fibonacci_memoization(n-1)
    return memo[n]

n = 10
memo = [0] * (n+1)
memo[0], memo[1] = 0, 1

print(fibonacci_memoization(n))