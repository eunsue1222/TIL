# 클래스 정의
class Person:
    # attribute
    blood_color = 'red'
    
    # method
    # __init__: 객체를 생성할 때 자동으로 호출되는 메서드로, 인스턴스를 생성하고 필요한 초기값을 설정
    # self: 인스턴스마다 독립적인 값을 가지며, 인스턴스가 생성될 때마다 초기화
    def __init__(self, name):
        self.name = name
    def singing(self):
        return f'{self.name}가 노래합니다.'


# 인스턴스 생성
singer1 = Person('iu')
# 메서드 호출
print(singer1.singing())  
# 속성(변수) 접근
print(singer1.blood_color)