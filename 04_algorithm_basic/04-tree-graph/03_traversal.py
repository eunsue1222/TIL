# 완전 이진 트리 기준 순회

# 전위 순회
def preorder_traversal(idx):
    pass

# 중위 순회
def inorder_traversal(idx):
    pass

# 후위 순회
def postorder_traversal(idx):
    pass

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
print('중위 순회')
inorder_traversal(1)  # 'D' 'B' 'E' 'A' 'C'
print('후위 순회')
postorder_traversal(1)  # 'D' 'E' 'B' 'C''A'