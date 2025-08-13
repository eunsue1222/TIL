# 그리디
def get_minimum_coins(coins, change):
    result = {} # 사용된 동전
    coins.sort(reverse=True) # 큰 단위 동전부터 사용 (오름차순)

    for coin in coins:
        count = 0 # 사용된 동전의 개수
        while change >= coin: # 거슬러 줄 수 있는 경우
            change -= coin
            count += 1
            result[coin] = count

    return result

coins = [1, 5, 10, 50, 100, 500]  # 동전 종류
change = 882  # 잔돈

# 아래의 경우라면 어떨까?
# coins = [1, 5, 10, 50, 100, 400, 500]  # 동전 종류
# change = 882  # 잔돈

result = get_minimum_coins(coins, change)
for coin, count in result.items():
    print(f"{coin}원: {count}개")