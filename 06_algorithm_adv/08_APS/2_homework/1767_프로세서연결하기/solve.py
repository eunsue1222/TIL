'''
# 모바일 프로세서 멕시노스 N x N
# 1개의 cell: 1개의 Core 또는 1개의 전선
# 전원: 가장자리
# Core: 1개 이상 12개 이하, 연결되지 않는 Core 존재 가능
# 전선: Core와 전원을 연결, 직선으로만 설치, 교차 불가능
# 최대한 많은 Core에 전원을 연결하였을 때 전선 길이 합의 최소값?
'''

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # N: 멕시노스 크기 (7 ≤  N ≤ 12)
    processor = [list(map(int, input().split())) for _ in range(N)] # 0: 빈 cell, 1: core

    # print(f'#{test_case} {result}')