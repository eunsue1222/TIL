# import sys
# sys.stdin = open('sample_input.txt', 'r')

def dfs(depth, plus, minus, times, divided, result):
    global min_val, max_val

    # 종료 조건: 계산 완료
    if depth == N:
        min_val = min(min_val, result)
        max_val = max(max_val, result)
        return

    # 탐색: 각 연산자의 모든 조합 만들기
    if plus:
        dfs(depth+1, plus-1, minus, times, divided, result + numbers[depth])
    if minus:
        dfs(depth+1, plus, minus-1, times, divided, result - numbers[depth])
    if times:
        dfs(depth+1, plus, minus, times-1, divided, result * numbers[depth])
    if divided:
        if result < 0:
            dfs(depth+1, plus, minus, times, divided-1, -(-result // numbers[depth]))
        else:
            dfs(depth+1, plus, minus, times, divided-1, result // numbers[depth])

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # N: 숫자의 개수
    operators = list(map(int, input().split())) # 연산자
    numbers = list(map(int, input().split())) # 숫자

    min_val = 100000000
    max_val = -100000000

    dfs(1, *operators, numbers[0])

    print(f'#{test_case} {max_val - min_val}')