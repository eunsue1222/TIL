# import sys
# sys.stdin = open('input.txt', 'r')

def postorder_traversal(idx):
    value, left, right = binary_tree[idx]
    if type(value) == int: # 정수인 경우
        return value
    else: # 연산자인 경우
        # 왼쪽 자식
        left_child = postorder_traversal(left)
        # 오른쪽 자식
        right_child = postorder_traversal(right)
        # 부모
        if value == '+':
            return left_child + right_child
        elif value == '-':
            return left_child - right_child
        elif value == '*':
            return left_child * right_child
        elif value == '/':
            return left_child / right_child


T = 10
for test_case in range(1, T+1):
    N = int(input())
    binary_tree = [None] * (N+1)

    for _ in range(N):
        operator = list(input().split()) # 입력: 정수 -> '정점번호 양의정수', 연산자 -> '정점번호 연산자 왼쪽자식번호 오른쪽자식번호'
        for idx in range(len(operator)): # 정수: str -> int 변환
            if operator[idx].isdigit():
                operator[idx] = int(operator[idx])

        if len(operator) == 2: # 정수인 경우
            binary_tree[operator[0]] = (operator[1], None, None) # binary_tree[idx] = [값, None, None]
        else: # 연산자인 경우
            binary_tree[operator[0]] = operator[1:] # binary_tree[idx] = [연산자, 왼쪽, 오른쪽]

    result = postorder_traversal(1)
    print(f'#{test_case} {int(result)}')