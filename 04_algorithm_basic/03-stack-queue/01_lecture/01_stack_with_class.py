class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity # 최대 수용 가능 공간
        self.items = [None] * capacity
        self.top = -1 # push 연산 진행 시, top 값을 1 증가시키고 값을 삽입

    # 삽입
    def push(self, item):
        if self.is_full():
            raise IndexError('Stack is Full')
        self.top += 1 # 삽입 위치
        self.items[self.top] = item

    # 삭제
    def pop(self):
        if self.is_empty():
            print('Stack is Empty')
            return
        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item

    # 예외처리
    def is_full(self):
        return self.capacity-1 == self.top

    # 예외처리
    def is_empty(self):
        return self.top == -1

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
print(stack.items)

print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.is_empty())
print(stack.pop())
print(stack.pop())