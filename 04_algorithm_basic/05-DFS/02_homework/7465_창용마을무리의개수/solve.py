# import sys
# sys.stdin = open('s_input.txt', 'r')

def dfs(node):
    # 방문 처리
    visited[node] = True

    # 탐색
    for n in graph[node]:
        if not visited[n]:
            dfs(n)


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N: 사람의 수, M: 사람 관계의 수

    # 그래프 생성
    graph = [[] for _ in range(N+1)] # 인접 리스트
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 초기값 설정
    group = 0
    visited = [False] * (N+1)

    for i in range(1, N+1): # 사람마다
        if not visited[i]: # 새로운 사람이면
            dfs(i) # 관계 조사
            group += 1

    print(f'#{test_case} {group}')