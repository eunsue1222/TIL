'''
아래와 같은 이진 트리가 있다면,
        'A'
       /   \
    'B'     'C'
    /  
  'D'
  /
'E'
'''
# 1번 index를 root로 설정하였을 때,
# 'A'의 왼쪽, 오른쪽 자식은 각각 2, 3 index에 해당함
# 'B'의 왼쪽, 오른쪽 자식은 각각 4, 5 index에 해당함
# 'D'의 왼쪽, 오른쪽 자식은? 

# 위 이진트리를 리스트로 나타낸다면
tree = [None, 'A', 'B', 'C', 'D', None, None, None, 'E', None, None, None, None, None, None, None]

print('존재하는 모든 요소 출력하기')
for index in range(1, 2**4):
    if tree[index]:
        print(tree[index])

print('부모 찾기')
# 'E' 노드의 조상 노드 찾기: 내 인덱스 //2
index = 8
while index > 1:
    parent = tree[index // 2]
    print(parent, end=' ')
    index //= 2

print()
print('왼쪽 or 오른쪽 자식 찾기')
# 왼쪽 자식 찾기: 내 인덱스 * 2
# 오른쪽 자식 찾기: 내 인덱스 * 2 + 1
index = 1
while index < 8:
    left_child = tree[index * 2]
    right_child = tree[index * 2 + 1]
    print(left_child)
    print(right_child)
    index *= 2