def fibo(N):
    global cnt
    cnt += 1

    if N >= 2 and memo[N] == 0:
        memo[N] = fibo(N-1) + fibo(N-2)
    return memo[N]


cnt = 0

memo = [0] * (101) # 초기화
memo[0] = 0 # 기저 조건
memo[1] = 1 # 기저 조건

result = fibo(100)
print(result)
print(cnt)