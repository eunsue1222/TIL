# import sys
# sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    expression = input().strip()

    stack = []
    total = 0

    for i in range(len(expression)):
        if expression[i] == '(': # '('인 경우
            stack.append('(')
        else: # ')'인 경우
            stack.pop()
            if expression[i-1] == '(': # '(': 레이저
                total += len(stack)
            else: # ')': 막대기
                total += 1

    print(f'#{test_case} {total}')