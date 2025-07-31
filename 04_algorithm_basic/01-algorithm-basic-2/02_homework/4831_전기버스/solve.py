T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split()) # K: 최대로 이동할 수 있는 정류장 수, N: 종점, M: 충전기가 설치된 정류장 개수
    charging_point = list(map(int, input().split())) # 충전기가 설치된 정류장



    print(f'#{test_case} {}')