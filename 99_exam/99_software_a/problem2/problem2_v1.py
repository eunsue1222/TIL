# N개의 문제 중 M개 정답
# 1. 카운터의 값은 처음에 0이다.
# 2. 문제를 틀리는 경우, 카운터는 항상 0으로 리셋되고 해당 문제에 대해서는 0점이 부여된다.
# 3. 문제를 맞추는 경우, 카운터는 1 증가되고 해당 문제에 대해서는 1점이 더해진다.
# 4. 카운터가 주어진 K가 된 경우, 해당 문제에 대해 1점이 더해지고, 카운터는 0으로 리셋되면서 동시에 전체 점수가 2배가 된다.
# M개의 문제를 맞추는 경우 중 총점이 최소인 경우?

### => FAIL 제한시간 초과

def dfs(count, number, solved, score):
    global min_value
    # global count

    # 가지 치기
    if score >= min_value:
        return

    # 종료 조건
    if solved == M:
        min_value = min(min_value, score)
        return

    if number == N:
        return

    # 문제 맞은 경우
    if count == K:
        count = 0
        score += 1
        score *= 2
        dfs(count, number+1, solved+1, score)
    else:
        count += 1
        score += 1
        dfs(count, number+1, solved+1, score) # 카운터 1 증가, 문제+1점

    # 문제 틀린 경우
    count = 0
    dfs(count, number+1, solved, score) # 카운터 0으로 리셋


T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split()) # N: 문제 개수 (3 <= N <= 500), M: 맞은 문제 개수 (2 <= M <= N), K: 카운터 (2 <= K <= N)

    min_value = float('inf')

    count = 0
    number = 0
    solved = 0
    score = 0
    dfs(count, number, solved, score) # 현재 문제 번호, 맞은 문제 개수, 현재 점수

    print(f'#{test_case} {min_value}')