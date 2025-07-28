# Sequence Types: 여거 개의 값들을 순서대로 나열하여 저장하는 자료형 (str, list, tuple. range)
# 순서(Sequence): 값들이 순서대로 저장 (정렬 x)
# 인덱싱(Indexing): 각 값에 고유한 인덱스(번호)를 가지고 있음. 인덱스를 사용하여 특정 위치의 값을 선택하거나 수정할 수 있음.
# 슬라이싱(Slicing): 인덱스 범위를 조절해 부분적인 값을 추출할 수 있음
# 길이(Length): len() 함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음
# 반복(Iteration): 반복문을 사용하여 저장된 값들을 반복적으로 처리할 수 있음

# Hello, World!
print('Hello, World!') 
# str
print(type('Hello, World!')) 


bugs = 'roaches'
counts = 13
area = 'living room'
# Debugging roaches 13 living room
print(f'Debugging {bugs} {counts} {area}')


my_str = 'hello'
# 인덱싱
print(my_str[1]) # e
# 슬라이싱
print(my_str[2:4]) # ll
# 길이
print(len(my_str)) # 5

# TypeError: 'str' object does not support item assignment
my_str[1] = 'z'


# replace
text = 'Hello, world!'
new_text = text.replace('world', 'Python')
print(new_text)  # Hello, Python!

# strip
text = '  Hello, world!  '
new_text = text.strip()
print(new_text)  # 'Hello, world!'


# split
text = 'Hello, world!'
words = text.split(',')
print(words)  # ['Hello', ' world!']

# join
words = ['Hello', 'world!']
text = '-'.join(words)
print(text)  # 'Hello-world!'
