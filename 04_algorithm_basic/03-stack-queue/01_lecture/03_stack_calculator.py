def infix_to_postfix(expression):
    op_dict = {'+':1, '-':1, '*':2, '/':2, '(':0} # 연산자의 우선순위
    stack = [] # 연산자를 저장할 스택
    postfix = [] # 후위 표기식을 저장할 리스트

    for char in expression:
        if char.isnumeric(): # 숫자
            postfix.append(char)
        elif char == '(':
            stack.append(char) # 스택에 넣기
        elif char == ')':
            top_token = stack.pop() # 스택에서 빼기
            while top_token != '(':
                postfix.append(top_token)
                top_token = stack.pop()
        else:
            while stack and op_dict[stack[-1]] >= op_dict[char]: # 연산자의 우선순위에 따라 다르게 처리
                postfix.append(stack.pop())
            stack.append(char)
    while stack:
        postfix.append(stack.pop())

    return ' '.join(postfix)


# 후위 표기식 계산 함수 
def run_calculator(expr):
    pass

# 예시
infix_expression = "3+(2*5)-8/4"

# 중위 표기식을 후위 표기식으로 변환
postfix_expression = infix_to_postfix(infix_expression)
print(f"후위 표기식: {postfix_expression}")     # 결과 확인

# 후위 표기식을 계산
result = run_calculator(postfix_expression)
print(result)       # 결과 확인
