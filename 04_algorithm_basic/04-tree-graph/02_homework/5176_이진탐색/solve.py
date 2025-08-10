# import sys
# sys.stdin = open('sample_input.txt', 'r')

def inorder_traversal(idx):
    global count

    if idx <= N:  # 순회 범위
        inorder_traversal(idx * 2)  # 왼쪽 서브 트리에 재귀함수 호출
        tree[idx] = count  # 부모 노드 먼저 조사
        count += 1
        inorder_traversal(idx * 2 + 1)  # 오른쪽 서브 트리에 재귀함수 호출

    return


T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # N: 노드 개수

    tree = [0] * (N+1) # 이진 트리
    count = 1 # 1번 ~ N번
    inorder_traversal(1) # 루트 노드

    print(f'#{test_case} {tree[1]} {tree[N//2]}')