'''
# 보호필름: D (막) x W (셀)
# 약품: 투입하는 경우 모든 셀들은 하나의 특성으로 변경
# 합격기준: 모든 세로방향에 대해서 동일한 특성의 셀들이 K개 이상
# 성능검사를 통과할 수 있는 최소 약품 투입 횟수?
'''

import sys
sys.stdin = open('sample_input.txt')

def check_film(arr):
    for i in range(len(arr)-K):
        if arr[i:i+K]

def performance_test(films):
    # 약품 사용 개수
    for col in zip(*films): # 각 세로방향 조사
        check_film(list(col)) # 합격기준 테스트


T = int(input())
for test_case in range(1, T+1):
    D, W, K = map(int, input().split()) # D: 보호 필름 두께 (3≤D≤13), W: 보호 필름 가로크기 (1≤W≤20), K: 합격기준 (1≤K≤D)
    films = [list(map(int, input().split())) for _ in range(D)] # 보호 필름 특성 (0: A, 1: B)

    performance_test(films) # 성능 검사

    # print(f'#{test_case} {result}')