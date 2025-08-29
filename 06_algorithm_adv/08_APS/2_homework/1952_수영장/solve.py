'''
# 이용권
    # 1일 이용권: 1일 이용
    # 1달 이용권: 1달 이용, 매달 1일 시작
    # 3달 이용권: 3달 이용, 매달 1일 시작, 연속 3달 사용
    # 1년 이용권: 1년 이용, 매년 1일 시작
# 이용 계획
    # 해당 달에 수영장을 이용한 날의 수
# 수영장을 이용할 수 있는 가장 적은 비용?
'''

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    prices = list(map(int, input().split())) # [1일, 1달, 3달, 1년 이용권 요금] (10 <= 요금 <= 3000)
    months = list(map(int, input().split())) # 1월부터 12월까지의 이용 계획

    # print(f'#{test_case} {result}')