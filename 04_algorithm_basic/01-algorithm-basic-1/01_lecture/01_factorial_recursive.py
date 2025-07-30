# 팩토리얼을 재귀함수로 구현

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))  # 5*4*3*2*1