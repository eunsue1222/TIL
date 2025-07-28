# Animal 클래스를 정의한다.
# Animal 클래스는 이름을 인자로 받는 생성자 메서드를 가진다.
# Animal 클래스는 speak 메서드를 가진다. 이 메서드는 자식 클래스에서 오버라이딩된다.
# Dog와 Cat 클래스를 정의하고, Animal 클래스를 상속받는다.
# Dog 클래스는 speak 메서드를 오버라이딩하여 "Woof!"를 반환한다.
# Cat 클래스는 speak 메서드를 오버라이딩하여 "Meow!"를 반환한다.
# Flyer와 Swimmer 클래스를 정의한다.
# Flyer 클래스는 fly 메서드를 가진다. 이 메서드는 "Flying"을 반환한다.
# Swimmer 클래스는 swim 메서드를 가진다. 이 메서드는 "Swimming"을 반환한다.
# Duck 클래스를 정의하고, Flyer와 Swimmer 클래스를 다중 상속받는다.
# Duck 클래스는 Animal 클래스를 상속받고, 이름을 인자로 받는 생성자 메서드를 가진다.
# Duck 클래스는 speak 메서드를 오버라이딩하여 "Quack!"을 반환한다.
# make_animal_speak 함수를 정의한다.
# 이 함수는 Animal 타입의 객체를 인자로 받아, 해당 객체의 speak 메서드를 호출하고 결과를 출력한다.
# 코드를 실행하고, 출력 결과를 확인한다.

# 아래에 코드를 작성하시오.
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class Flyer:
    def fly(self):
        return "Flying"
    
class Swimmer:
    def swim(self):
        return "Swimming"
    
class Duck(Flyer, Swimmer, Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Quack!"
    
def make_animal_speak(obj):
    print(obj.speak())
    
dog = Dog('Hund')
cat = Cat('Katze')
duck = Duck('Ente')

make_animal_speak(dog)
make_animal_speak(cat)
make_animal_speak(duck)
print(duck.fly())
print(duck.swim())