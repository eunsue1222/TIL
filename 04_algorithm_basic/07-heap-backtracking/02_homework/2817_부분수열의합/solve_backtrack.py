# import sys
# sys.stdin = open('sample_input.txt', 'r')

def backtrack(index, total):
    global count

    # 가지 치기
    if total > K:
        return

    # 종료 조건
    if total == K:
        count += 1
        return

    # 탐색
    for i in range(index, N):
        backtrack(i+1, total+numbers[i])


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    count = 0
    backtrack(0, 0) # for문

    print(f'#{test_case} {count}')