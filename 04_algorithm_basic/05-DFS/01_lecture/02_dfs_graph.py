def depth_first_search(vertex):
    global visited

    visited[vertex] = True # 현재 정점 방문 처리
    print(graph[vertex]) # 현재 방문한 정점

    for idx in range(N): # 다음에 방문 가능한 정점
        if adj_matrix[vertex][idx] and visited[idx] == False:
            depth_first_search(idx)


        # 0    1    2    3    4    5    6
graph = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# 정점 수: N
N = 7

# 해당 정점 방문 여부 표시: False로 초기화
visited = [False] * N

# 인접 행렬
adj_matrix = [
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
]

depth_first_search(0)
