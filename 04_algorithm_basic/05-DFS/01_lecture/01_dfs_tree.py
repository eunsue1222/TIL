# tree = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
#
# # 인접행렬
# adj_matrix = [
#     [0, 1, 1, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# DFS
def depth_first_search(node): # node: 현재 방문한 노드
    print(node)

    if node not in adj_list: # 자식 노드가 없는 경우
        return

    for next in adj_list.get(node): # 자식 노드들 방문
        depth_first_search(next) # next: 다음에 방문할 노드

# 인접리스트
adj_list = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G', 'H', 'I']
}

depth_first_search('A')