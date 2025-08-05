# import sys
# sys.stdin = open('input.txt', 'r')

def dfs(depth, cards):
    global max_val

    # 가지 치기
    key = (depth, ''.join(cards))
    if key in visited:
        return
    visited.add(key)

    # 종료 조건
    if depth == exchange:
        cards_int = int(''.join(cards))
        max_val = max(max_val, cards_int)
        return

    # 탐색
    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            cards[i], cards[j] = cards[j], cards[i]
            dfs(depth+1, cards)
            cards[i], cards[j] = cards[j], cards[i]


T = int(input())
for test_case in range(1, T+1):
    number, exchange = input().split()
    number = list(number)
    exchange = int(exchange)

    max_val = 0
    visited = set()
    dfs(0, number)

    print(f'#{test_case} {max_val}')