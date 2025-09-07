import sys
sys.stdin = open("input.txt")

def baby_gin():
    # A와 B의 카드?
    # 0번째: A카드, 1번째: B카드 카운팅 목록
    cards = [[0 for _ in range(10)], [0 for _ in range(10)]]

    for idx in range(len(data)):
        n = data[idx]
        cards[idx % 2][n] += 1
        if cards[idx % 2][n] == 3: return idx % 2 + 1
        if check_run(cards[idx % 2]): return idx % 2 + 1
    return 0

def check_run(cards):
    for i in range(8):
        if cards[i] >= 1 and cards[i+1] >= 1 and cards[i+2] >= 1:
            return 1

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    winner = baby_gin()
    print(f'#{tc} {winner}')