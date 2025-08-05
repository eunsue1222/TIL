# import sys
# sys.stdin = open('input.txt', 'r')

def dfs(depth, prob):
    global max_prob

    if prob <= max_prob: # 가지치기
        return

    if depth == N:
        max_prob = max(prob, max_prob)
        return

    for i in range(N):
        if not visited[i] and P[depth][i] != 0:
            visited[i] = True
            dfs(depth+1, prob*(P[depth][i]/100))
            visited[i] = False

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    max_prob = 0.0

    dfs(0, 1.0)

    print(f'#{test_case} {max_prob*100:.6f}')