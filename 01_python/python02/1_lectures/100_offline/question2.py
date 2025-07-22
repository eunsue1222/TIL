class ParentA:
    def __init__(self):
        self.home = 'Busan'

class ParentB:
    def __init__(self):
        self.home = 'Daejeon'

class Child(ParentA, ParentB):
    def __init__(self):
        '''
            이러한 경우에, super().__init__() 을 하게 되면
            ParentA의 생성자 함수를 불러와 사용하게 됩니다.
            하지만, 저는 ParentB의 생성자 함수를 사용하여 Child의 생성자 함수를 정의하고 싶습니다.
            이런 경우, 반드시 상속의 순서를 바꿔야만 하나요...?
                -> 여러가지 방법이 있습니다만... 아래와 같이 코드를 쓰시면 됩니다.
        '''
        # ParentB 클래스의 생성자를 호출하시면 되겠죠?
        ParentB.__init__()