# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # N: 농장의 크기
    farm = [list(map(int, input())) for _ in range(N)] # NxN 농장기

    mid = N // 2 # 가운데 지점
    total = 0

    for i in range(N):
        if mid >= i:
            total += sum(farm[i][mid-i:mid+i+1])
        else:
            total += sum(farm[i][i-mid:N-(i-mid)])

    print(f'#{test_case} {total}')