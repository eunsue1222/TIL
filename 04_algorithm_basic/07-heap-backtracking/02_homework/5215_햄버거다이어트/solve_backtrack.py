# import sys
# sys.stdin = open('sample_input.txt', 'r')

def backtrack(index, score, calorie):
    global best_score

    # 가지 치기
    if calorie > L:
        return

    best_score = max(best_score, score)

    for i in range(index, N):
        backtrack(i+1, score+table[i][0], calorie+table[i][1])


T = int(input())
for test_case in range(1, T+1):
    N, L = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]

    best_score = 0
    backtrack(0, 0, 0) # 중복 x, 조합

    print(f'#{test_case} {best_score}')