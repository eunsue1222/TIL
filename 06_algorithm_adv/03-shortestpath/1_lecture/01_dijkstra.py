import heapq, math

def dijkstra(graph, start):
    distances = {v: math.inf for v in graph} # {'a': inf, 'b': inf, 'c': inf, 'd': inf, 'e': inf, 'f': inf}
    distances[start] = 0 # 초기화

    heap = [] # 최소 힙
    heapq.heappush(heap, [0, start]) # [도달한 거리, 시작정점]
    visited = set()
    visited.add(start)

    while heap:
        dist, current = heapq.heappop(heap) # [도달한 거리, 시작정점]
        if current in visited or distances[current] < dist: # 방문한 적 있고, 갱신된 거리가 더 큰 경우
            continue
        visited.add(current)

        for next, weight in graph[current].items(): # 인접한 노드들에 대해서
            next_distance = dist + weight # 현재까지 가중치 + 다음까지 가중치
            if next_distance < distances[next]: # 방문한 적 없고, 갱신된 거리가 작은 경우
                distances[next] = next_distance # 거리 갱신
                heapq.heappush(heap, [next_distance, next]) # [도달한 거리, 시작정점]

    return distances


graph = {
    'a': {'b': 3, 'c': 5},
    'b': {'c': 2},
    'c': {'b': 1, 'd': 4, 'e': 6},
    # 'c': {'b': -4, 'd': 4, 'e': 6},
    'd': {'e': 2, 'f': 3},
    'e': {'f': 6},
    'f': {}
}

start_v = 'a'
res = dijkstra(graph, start_v)
print(res)  # {'a': 0, 'b': 3, 'c': 5, 'd': 9, 'e': 11, 'f': 12}
