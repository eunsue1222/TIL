def bellman_ford(graph, start):
    n = len(graph) # 정점의 수
    distances = {v: float('inf') for v in graph} # 거리 초기화
    distances[start] = 0 # 시작정점 거리 초기화

    for _ in range(n-1):
        updated = False # 갱신 여부 확인
        for u in graph: # 각 정점별 인접 정점 순회
            for v, weight in graph[u].items():
                if distances[u] != float('inf') and distances[u] + weight < distances[v]: # u까지의 거리 + v까지의 거리 < 최소 거리
                    distances[v] = distances[u] + weight # 거리 갱신
                    updated = True # 갱신 여부
        if updated == False:
            break

    # 음수 사이클 검사
    for u in graph:  # 각 정점별 인접 정점 순회
        for v, weight in graph[u].items():
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:  # u까지의 거리 + v까지의 거리 < 최소 거리
                print('음수 사이클이 있습니다')
                return False

    return distances


# 예시 그래프
graph = {
    'a': {'b': 4, 'c': 2},
    'b': {'c': 3, 'd': 2, 'e': 3},
    'c': {'b': 1, 'd': 4, 'e': 5},
    'd': {'e': -3},
    'e': {'f': 2},
    'f': {}
}

음수 사이클 예시 그래프
graph = {
    'a': {'b': 4, 'c': 2},
    'b': {'c': -3, 'd': 2, 'e': 3},
    'c': {'b': 1, 'd': 4, 'e': 5},
    'd': {'e': -3},
    'e': {'f': 2},
    'f': {}
}

# 시작 정점 설정
start_vertex = 'a'

# 벨만-포드 알고리즘 실행
result = bellman_ford(graph, start_vertex)

print(f"'{start_vertex}': {result}")
