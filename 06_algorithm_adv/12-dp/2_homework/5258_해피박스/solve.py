# import sys
# sys.stdin = open('sample_input.txt')

def knapsack(items, capacity):
    dp = [[0] * (capacity+1) for _ in range(M+1)] # dp[i][j]: 물건 i개, 용량 w -> 최대 가격

    for i in range(1, M+1): # 물건 개수 만큼
        for j in range(1, capacity+1): # 용량 만큼
            if items[i-1][0] > j: # 현재 물건 담을 수 없는 경우
                dp[i][j] = dp[i-1][j] # 물건을 담지 않는 경우
            else: # 현재 물건 담을 수 있는 경우
                dp[i][j] = max(items[i-1][1] + dp[i-1][j-items[i-1][0]], dp[i-1][j]) # 물건을 담는 경우 / 물건을 담지 않는 경우

    return dp[M][capacity] # 최대 가격


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N: 박스의 크기 (10<=N<=100), M: 상품의 개수 (1<=M<=20)
    products = [list(map(int, input().split())) for _ in range(M)] # S: 상품의 크기 (1<=Si<=20), P: 상품의 가격 (1<=Pi<=20)

    result = knapsack(products, N)
    print(f'#{test_case} {result}')