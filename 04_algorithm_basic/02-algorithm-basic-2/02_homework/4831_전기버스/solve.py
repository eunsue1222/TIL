# import sys
# sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split()) # K: 최대로 이동할 수 있는 정류장 수, N: 종점, M: 충전기가 설치된 정류장 개수
    charging_point = set(map(int, input().split())) # 충전기가 설치된 정류장

    total = 0 # 총 충전 횟수
    current = 0 # 현재 위치

    while current+K < N:
        for stop in range(current+K, current, -1): # 이동 가능한 범위
            if stop in charging_point: # 충전기가 있는 경우
                total += 1 # 충전 완료
                current = stop # 현재 위치 변경 (가장 먼 충전기)
                break
        else: # 충전기가 없는 경우
            total = 0
            break

    print(f'#{test_case} {total}')