# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    bin_M = bin(M)[2:]
    bin_M = bin_M.zfill(N)

    if '0' in bin_M[len(bin_M)-N:len(bin_M)+1]:
        result = 'OFF'
    else:
        result = 'ON'

    print(f'#{test_case} {result}')