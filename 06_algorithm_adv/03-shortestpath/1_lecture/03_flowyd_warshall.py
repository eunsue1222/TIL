def floyd_warshall(graph):
    n = len(graph) # 노드 개수
    for k_node in range(n): # 모든 정점을 경유 정점으로 고려
        for start in range(n): # 시작노드
            for end in range(n): # 도착노드
                # Dik + Dkj < Dij
                Dik = graph[start][k_node] # i에서 k로 가는 거리
                Dkj = graph[k_node][end] # k에서 j로 가는 거리
                Dij = graph[start][end] # i에서 j로 가는 거리
                if Dik + Dkj < Dij: # k를 경유하는 것이 더 나은 경우
                    graph[start][end] = Dik + Dkj # 갱신
    return graph


INF = float('inf')  # 무한대

# # 예시 그래프의 인접 행렬
# adj_matrix = [
#     [0, 4, 2, 5, INF],
#     [INF, 0, 1, INF, 4],
#     [1, 3, 0, 1, 2],
#     [-2, INF, INF, 0, 2],
#     [INF, -3, 3, 1, 0]
# ]

# # 음수 사이클 확인
# adj_matrix = [
#     [0, -4, 2, 5, INF],
#     [INF, 0, 1, INF, 4],
#     [1, 3, 0, 1, 2],
#     [-2, INF, INF, 0, 2],
#     [INF, -3, 3, 1, 0]
# ]

result = floyd_warshall(adj_matrix)

# 최단 거리 행렬 출력 
for row in result:
    print(row)
'''
# 예시 그래프의 인접 행렬
[0, 1, 2, 3, 4]
[0, 0, 1, 2, 3]
[-1, -1, 0, 1, 2]
[-2, -1, 0, 0, 2]
[-3, -3, -2, -1, 0]
'''
'''
# 음수 사이클 확인
[-55, -59, -58, -61, -97]
[-51, -55, -54, -57, -93]
[-54, -58, -57, -60, -96]
[-63, -67, -66, -69, -105]
[-96, -100, -99, -102, -138]
'''