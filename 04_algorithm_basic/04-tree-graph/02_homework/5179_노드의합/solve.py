# import sys
# sys.stdin = open('sample_input.txt', 'r')

# 후위 순회: 왼쪽 자식 -> 오른쪽 자식 -> 부모
def postorder_traversal(idx):
    if idx > N: # 트리 범위 확인
        return 0 # 왼쪽/오른쪽 자식 노드가 존재하지 않는 경우 TypeError 처리 위함

    if tree[idx] is not None: # 리프 노드인 경우
        return tree[idx] # 값 존재

    tree[idx] = postorder_traversal(idx*2) + postorder_traversal(idx*2+1) # 리프 노드가 아닌 경우
    return tree[idx] # 자식 노드에 저장된 값의 합


T = int(input())
for test_case in range(1, T+1):
    # N: 노드의 개수, M: 리프 노드의 개수, L: 값을 출력할 노드 번호
    N, M, L = map(int, input().split())

    # 트리 생성
    tree = [None] * (N+1)
    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    # 트리 순회
    postorder_traversal(1)
    print(f'#{test_case} {tree[L]}')