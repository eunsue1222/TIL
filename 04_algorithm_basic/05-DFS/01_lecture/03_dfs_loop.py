def DFS(now):
    stack = [] # 스택

    visited.add(now) # 현재 노드 방문 처리
    stack.append(now) # 현재 노드 스택에 넣기

    while stack: # 스택이 빌 때까지
        target = stack.pop() # 현재 방문한 노드
        print(target)

        for next in graph[target]: # 현재 방문 노드의 인접 리스트
            if next not in visited: # 다음에 방문할 노드
                visited.add(next)
                stack.append(next)


# 그래프 인접 리스트
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['B', 'F'],
    'F': ['D', 'E', 'G'],
    'G': ['C']
}

start_vertex = 'A'
visited = set() # 방문한 정점을 저장할 집합

DFS(start_vertex)