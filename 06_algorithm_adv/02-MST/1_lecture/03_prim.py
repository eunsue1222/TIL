import heapq

def prim(vertices, edges):
    mst = [] # 최소 신장 트리를 그릴 수 있는 간선 목록
    visited = set() # 방문 확인
    start_vertex = vertices[0] # 시작 정점

    min_heap = [(w, s, e) for e, w in adj_list[start_vertex]] # 시작 정점에서 갈 수 있는 정점들에 대한 간선 정보 [(가중치, 시작정점, 종료정점)]
    heapq.heapify(min_heap) # heapq에 삽입
    visited.add(start_vertex)

    while min_heap: # 모든 후보군 순회
        # print(min_heap)
        weight, start, end = heapq.heappop(min_heap)
        if end in visited: continue

        visited.add(end) # 새로운 정점 방문
        mst.append((start, end, weight)) # 간선 정보 mst에 추가

        for next, weight in adj_list[end]:
            if next in visited: continue # 다음 방문 예정 정점이 이미 방문된 경우
            heapq.heappush(min_heap, (weight, end, next))

    return mst

'''
    가중치 그래프 형상
         1
      ¹ / \ ²
       2---3
         ³
'''
vertices = [1, 2, 3]
edges = [[1, 2, 1], [2, 3, 3], [1, 3, 2]]
# 그래프 기준 인접 정점 정보(인접 행렬, 인접 리스트) 필요
adj_list = {v: [] for v in vertices}
for s, e, w in edges:
    adj_list[s].append((e, w))
    adj_list[e].append((s, w))
print(adj_list)

'''
    MST 구성 결과
         1
      ¹ / \ ²
       2   3
'''
mst = prim(vertices, edges)  # [(1, 2, 1), (1, 3, 2)]
print(mst)


# 교재 간선 정보
edges = [
    (0, 1, 32),
    (0, 2, 31),
    (0, 5, 60),
    (0, 6, 51),
    (1, 2, 21),
    (2, 4, 46),
    (2, 6, 25),
    (3, 4, 34),
    (3, 5, 18),
    (4, 5, 40),
    (4, 6, 51),
]
vertices = list(range(7))  # 정점 집합

# 그래프 기준 인접 정점 정보(인접 행렬, 인접 리스트) 필요
adj_list = {v: [] for v in vertices}
for s, e, w in edges:
    adj_list[s].append((e, w))
    adj_list[e].append((s, w))

result = prim(vertices, edges)
print(result) # [(0, 2, 31), (2, 1, 21), (2, 6, 25), (2, 4, 46), (4, 3, 34), (3, 5, 18)]