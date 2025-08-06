from collections import deque

def BFS(start_vertex): # start_vertex: 시작 정점
    # 방문 여부
    # visited = [0] * len(nodes)
    visited = set()

    queue = deque([start_vertex]) # double-ended-queue
    visited.add(start_vertex)
    result = []

    while queue:
        node = queue.popleft() # FIFO
        result.append(node) # 경로

        # # 인접 리스트
        # for neighbor in adj_list.get(node, []): # 조사한 노드의 인접 리스트에서 자식 노드들 찾기
        #     if neighbor not in visited:
        #         visited.add(neighbor) # 방문 표시
        #         queue.append(neighbor) # 다음 방문 노드들 추가

        # 인접 행렬
        for next_index in range(len(nodes)):
            if next_index not in visited and adj_matrix[node][next_index]:
                visited.add(next_index)
                queue.append(next_index)

    return result


# 정점 정보
#         0    1    2    3    4    5    6
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# 간선 정보
edges = [
    '0 1',
    '0 2',
    '1 3',
    '1 4',
    '2 4',
    '3 5',
    '4 5',
    '5 6'
]

# 인접 리스트
adj_list = {node: [] for node in nodes} # 초기화
for edge in edges:
    u, v = edge.split() # u: 시작 정점, v: 도착 정점
    adj_list[nodes[int(u)]].append(nodes[int(v)]) # 무방향 그래프
    adj_list[nodes[int(v)]].append(nodes[int(u)]) # 무방향 그래프
print(adj_list)

# 인접 행렬
adj_matrix = [[0] * len(nodes) for _ in range(len(nodes))] # 초기화
for edge in edges:
    u, v = edge.split() # u: 시작 정점, v: 도착 정점
    u_index, v_index = int(u), int(v)
    adj_matrix[u_index][v_index] = 1 # 무방향 그래프
    adj_matrix[v_index][u_index] = 1 # 무방향 그래프
print(adj_matrix)

print(BFS('A'))