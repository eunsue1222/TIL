# import sys
# sys.stdin = open("input.txt", "r")

from itertools import permutations

# run 여부: 3장의 카드가 연속적인 번호
def is_run(half_cards):
    return half_cards[0]+1 == half_cards[1] and half_cards[1]+1 == half_cards[2]

# triplet 여부: 3장의 카드가 동일한 경우
def is_triplet(half_cards):
    return half_cards[0] == half_cards[1] == half_cards[2]

# babygin 여부: 6장의 카드가 run과 triplet로만 구성된 경우
def is_babygin(cards):
    for perm in permutations(cards): # 카드 순열(순서o, 중복x) 생성
        first_group = perm[:3] # 그룹 나누기 (카드 3장씩)
        second_group = perm[3:] # 그룹 나누기 (카드 3장씩)
        if (is_run(first_group) or is_triplet(first_group)) and (is_run(second_group) or is_triplet(second_group)):
            return True
    return False


T = int(input())
for test_case in range(1, T+1):
    cards = list(map(int, input().strip()))
    if len(cards) != 6: # 잘못된 카드 개수
        print(f'#{test_case} false')
        continue
    status = "true" if is_babygin(cards) else "false"
    print(f'#{test_case} {status}')