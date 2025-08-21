T = int(input())
for test_case in range(1, T+1):
    N, E = map(int, input().split()) # N: 마지막 연결지점 번호, E: 도로의 개수
    info = [list(map(int, input().split())) for _ in range(E)]

    print(f'#{test_case} {result}')

