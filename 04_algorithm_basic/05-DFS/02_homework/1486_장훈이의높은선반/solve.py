# import sys
# sys.stdin = open('input.txt', 'r')

def dfs(index, total):
    global answer

    if total >= B: # 가지치기
        answer = min(answer, total - B)
        return

    if index == N:
        return

    dfs(index+1, total + heights[index]) # 선택 o
    dfs(index+1, total) # 선택 x

T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    answer = float('inf')
    dfs(0, 0)
    print(f'#{test_case} {answer}')