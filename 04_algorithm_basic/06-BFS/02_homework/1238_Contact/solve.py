# import sys
# sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(start_node, start_level):
    # 큐 생성
    queue = deque()
    queue.append((start_node, start_level))

    # 방문 처리
    visited.add(start_node)

    # 경로 추가
    path[start_level].append(start_node)

    while queue:
        node, level = queue.popleft()
        for n in graph.get(node, []):
            if n not in visited: # 처음 방문
                visited.add(n) # 방문 표시
                path[level+1].append(n) # 같은 레벨에 경로 추가
                queue.append((n, level+1)) # 이동


T = 10
for test_case in range(1, T+1):
    length, start = map(int, input().split()) # length: 데이터의 길이, start: 시작점
    data = list(map(int, input().split())) # data: 데이터 (from, to, from, to, ...)

    # 그래프 생성
    graph = {person:[] for person in set(data)} # 사람 수만큼 노드 생성
    for idx in range(0, length, 2):
        graph[data[idx]].append(data[idx+1]) # from -> to 인접리스트

    visited = set() # 방문 여부 체크
    path = [[] for _ in range(101)] # 연락 인원 최대 100명

    bfs(start, 0)

    for level in reversed(range(len(path))):
        if path[level]:
            answer = max(path[level])
            break

    print(f'#{test_case} {answer}')