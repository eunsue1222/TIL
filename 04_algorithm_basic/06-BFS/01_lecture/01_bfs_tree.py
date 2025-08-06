# BFS
def BFS(root_node): # root_node: 탐색을 시작할 서브 트리의 루트
    result = [] # 탐색 경로
    data_structure = [root_node] # 조사할 노드들을 담을 자료구조

    while data_structure: # 조사할 노드들이 있으면
        node = data_structure.pop(0) # FIFO: 조사할 노드 삭제
        result.append(node) # 조사한 노드를 경로에 추가
        for child in graph.get(node, []): # 조사한 노드의 인접 리스트에서 자식 노드들 찾기
            data_structure.append(child) # 자식 노드들 추가

    return result # 완성된 경로


# 그래프 인접 리스트
graph = {
    'A': ['B', 'C', 'D'], 
    'B': ['E', 'F'],
    'C': [],
    'D': ['G', 'H', 'I'], 
    'E': [],
    'F': [],
    'G': []
}

start_node = 'A'

print(BFS('A'))