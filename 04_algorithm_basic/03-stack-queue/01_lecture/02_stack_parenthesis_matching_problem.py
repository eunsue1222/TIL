def check_match(expression):
    stack = [] # 여는 괄호들을 담아둘 스택
    matching_dict = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    for char in expression:
        if char in matching_dict.values(): # 여는 괄호 여부
            stack.append(char)
        elif char in matching_dict.keys(): # 닫는 괄호 여부
            if not stack or stack[-1] != matching_dict[char]:
                return False
            stack.pop()
    return not stack

# 예시
examples = ["(a(b)", "a(b)c)", "a{b(c[d]e}f)"]
for ex in examples:
    if check_match(ex): 
        print(f"{ex} 는 올바른 괄호") 
    else:
        print(f"{ex} 는 올바르지 않은 괄호")  
