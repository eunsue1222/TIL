# import sys
# sys.stdin = open('input.txt', 'r')

# 중위순회: 왼쪽자식 -> 부모 -> 오른쪽자식
def inorder_traversal(idx):
    if idx <= N:
        inorder_traversal(idx*2)
        result.append(tree[idx])
        inorder_traversal(idx*2+1)

T = 10
for test_case in range(1, T+1):
    N = int(input()) # N: 정점의 수

    tree = [None] * (N+1)
    for _ in range(N):
        node = list(input().split())
        tree[int(node[0])] = node[1]

    result = []
    inorder_traversal(1)
    print(f'#{test_case} {"".join(result)}')