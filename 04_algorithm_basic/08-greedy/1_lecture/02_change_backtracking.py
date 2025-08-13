# 백트래킹
def get_minimum_coins_backtrack(coins, change):
    result = {}  # 사용된 동전
    coins.sort(reverse=True)  # 큰 단위 동전부터 사용 (오름차순)
    min_coins = change # 최소 동전 개수

    def backtrack(remain, target, curr_comb, acc): # remain: 남은 금액, target: 사용할 동전 인덱스, curr_comb: 지금까지 만들어진 조합, acc: 지금까지 사용한 동전의 개수
        nonlocal min_coins, result

        # 기저 조건: 남은 금액 = 0
        if remain == 0:
            if acc < min_coins:
                min_coins = acc
                result = dict(curr_comb) # 복사본
            return

        # 가지치기
        if acc >= min_coins:
            return

        # 유도 조건: 남은 동전들에 대해서 모두 시도
        for idx in range(target, len(coins)):
            coin = coins[idx]
            if coin <= remain:
                max_count = remain // coin
                curr_comb[coin] = max_count
                backtrack(remain-coin*max_count, idx+1, curr_comb, acc+max_count)
                curr_comb[coin] = 0

    backtrack(change, 0, {}, 0)

    return result


# 사용 예시
coins = [1, 5, 10, 50, 100, 400, 500]  # 동전 종류
change = 882  # 잔돈

result = get_minimum_coins_backtrack(coins, change)
for coin, count in result.items():
    if count > 0:
        print(f"{coin}원: {count}개")