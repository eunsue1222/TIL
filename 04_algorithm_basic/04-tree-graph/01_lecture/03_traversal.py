# 완전 이진 트리 기준 순회

# 전위 순회: 부모 -> 왼쪽 자식 -> 오른쪽 자식
# A B D E C
def preorder_traversal(idx):
    if idx <= N: # 순회 범위
        print(tree[idx], end=' ') # 부모 노드 먼저 조사
        preorder_traversal(idx * 2) # 왼쪽 서브 트리에 재귀함수 호출
        preorder_traversal(idx * 2 + 1) # 오른쪽 서브 트리에 재귀함수 호출


# 중위 순회: 왼쪽 자식 -> 부모 -> 오른쪽 자식
# D B E A C
def inorder_traversal(idx):
    if idx <= N:  # 순회 범위
        inorder_traversal(idx * 2)  # 왼쪽 서브 트리에 재귀함수 호출
        print(tree[idx], end=' ')  # 부모 노드 먼저 조사
        inorder_traversal(idx * 2 + 1)  # 오른쪽 서브 트리에 재귀함수 호출

# 후위 순회: 왼쪽 자식 -> 오른쪽 자식 -> 부모
# D E B C A
def postorder_traversal(idx):
    if idx <= N:  # 순회 범위
        postorder_traversal(idx * 2)  # 왼쪽 서브 트리에 재귀함수 호출
        postorder_traversal(idx * 2 + 1)  # 오른쪽 서브 트리에 재귀함수 호출
        print(tree[idx], end=' ')  # 부모 노드 먼저 조사

N = 5
tree = [0, 'A', 'B', 'C', 'D', 'E']


'''
    트리 구조
        'A'
      /   \
   'B'    'C'
  /   \
'D'    'E'
'''

print('전위 순회')
preorder_traversal(1)  # 'A' 'B' 'D' 'E' 'C'

print()
print('중위 순회')
inorder_traversal(1)  # 'D' 'B' 'E' 'A' 'C'

print()
print('후위 순회')
postorder_traversal(1)  # 'D' 'E' 'B' 'C''A'