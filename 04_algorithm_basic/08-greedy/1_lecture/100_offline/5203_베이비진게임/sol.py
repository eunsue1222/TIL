import sys
sys.stdin = open("input.txt")

def baby_gin():
    # A가 받는 카드 목록
    # a_cards = []
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # A가 받은 카드 목록을 카운팅
    a_cards = [0 for _ in range(10)]
    # B가 받은 카드 목록을 카운팅
    b_cards = [0 for _ in range(10)]

    for idx in range(len(data)):
        # 0번째는 A 1번째는 B...
        if idx % 2 == 0:
            a_cards[data[idx]] += 1
            # 카드 받자마자 트리플인지 확인
            if a_cards[data[idx]] == 3:
                return 1
            # 카드 받자마자 런인지 확인
            if check_run(a_cards):
                return 1
            # data[idx], data[idx+1], data[idx+2] 이 3개로만 run인지 확인하면 안됨!
            # data[idx-1], data[idx], data[idx+1]
            # data[idx-2], data[idx-1], data[idx]
        else:
            b_cards[data[idx]] += 1
            if b_cards[data[idx]] == 3:
                return 2
            if check_run(b_cards):
                return 2
    # 모든 턴을 다 써서 카드를 다 확인 했지만
    # return이 되지 못하고 이곳까지 와서 코드가 실행된다?
    return 0        # 무승부

def check_run(cards):
    # 0부터 9까지의 숫자 카드 중에서
        # 7 +1, 7+2 가 마지막 index
    for i in range(8):
        if cards[i] >= 1 and cards[i+1] >= 1 and cards[i+2] >= 1:
            return 1    # 그렇다면 런이다.

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    winner = baby_gin()
    print(f'#{tc} {winner}')