# import sys
# sys.stdin = open('sample_input.txt', 'r')

def dfs(index, score, calorie):
    global best_score

    # 가지 치기
    if calorie > L:
        return

    best_score = max(best_score, score)

    # 종료 조건
    if index == N:
        return

    dfs(index + 1, score + table[index][0], calorie + table[index][1]) # 선택 o
    dfs(index + 1, score, calorie) # 선택 x


T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]

    best_score = 0
    dfs(0, 0, 0) # 중복 x, 조합

    print(f'#{test_case} {best_score}')