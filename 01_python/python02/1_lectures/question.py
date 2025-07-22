# 단어를 드래그하거나 포커싱을 한 다음
# ctrl + D를 하면 (주의. 대소문자 구분 안됨) 동일한 글자 모두 다중 포커싱
# alt + 위아래 방향키로 줄바꿈
# alt shift + 위아래로 복제
# ctrl + 좌우: 단어 단위로 커서 이동
# ctrl + shift + 좌우: 단어 단위로 드래그
# ctrl + shift + home/end: 왼쪽 끝으로 드래그 / 오른쪽 끝으로 드래그
# 'ctrl + k' 'ctrl + s': VSCode shortcut 설정

class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'
    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')
class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'
    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        # self.value_c = 'Child'
        # self.value_a = 'Parent'
        super().__init__() # ParentA 클래스의 init 메서드 호출
        self.value_c = 'Child'
    def show_value(self):
        super().show_value() # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')

child = Child()
child.show_value() 