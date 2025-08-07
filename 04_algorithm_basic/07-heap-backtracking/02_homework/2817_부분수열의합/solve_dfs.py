# import sys
# sys.stdin = open('sample_input.txt', 'r')

def dfs(index, total):
    global count

    # 가지 치기
    if total > K:
        return

    # 종료 조건
    if index == N:
        if total == K:
            count += 1
        return

    # 탐색
    dfs(index+1, total+numbers[index]) # 선택 o
    dfs(index+1, total) # 선택 x


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    count = 0
    dfs(0, 0) # 중복 x, 조합 o

    print(f'#{test_case} {count}')