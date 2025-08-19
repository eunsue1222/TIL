# 각각 H의 높이를 가지는 N개의 나무
# 하루에 한 번 물주기 가능 -> 물 안주기: 나무의높이+0, 홀수날: 나무의높이+1, 짝수날:나무의높이+2
# 모든 나무의 키가 처음에 가장 키가 컸던 나무와 같아지도록 하는 최소 날짜 수?

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    numbers = int(input()) # N: 나무의 개수 (2 <= N <= 100)
    heights = list(map(int, input().split())) # H: 나무의 높이 (1 <= H <= 120)

    # 각 나무와 높이가 가장 큰 나무의 차이 구하기
    tallest_tree = max(heights)
    info = []
    for height in heights:
        difference = tallest_tree - height
        info.append([difference, difference//2, difference%2]) # [높이 차이, 짝수날, 홀수날]

    # 각 짝수날과 홀수날 합
    odd_day = sum(i[2] for i in info)
    even_day = sum(i[1] for i in info)

    # 짝수날과 홀수날 밸런스 맞추기
    while True:
        if even_day >= odd_day:
            even_day -= 1
            odd_day += 2
        else:
            even_day += 1
            odd_day -= 2
            break

    # 최소 날짜 수 계산
    if even_day > odd_day:
        result = even_day * 2
    elif even_day < odd_day:
        result = odd_day * 2 - 1
    else:
        result = even_day * 2

    print(f'#{test_case} {result}')