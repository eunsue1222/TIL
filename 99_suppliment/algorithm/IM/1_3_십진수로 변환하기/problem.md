## 10진수로 변환하기

---

### 문제
0과 1로 이루어진 이진수로 어떤 수가 주어지면 그 수를 십진수로 변환하여 출력하는 프로그램을 작성해보세요.

#### 입력
```
첫 번째 줄에 8자리 이하의 이진수로 되어있는 수가 주어집니다.
```
```
ex) 11101
```

#### 출력
```
첫 번째 줄에 주어진 이진수를 십진수로 변환하여 출력합니다.
```
```
ex) 29
```

#### 제한 조건
```
0 <= 이진수의 자릿수 <= 8
```

#### 제한
```
Time Limit: 1000 ms
Memory Limit: 80 MiB
```
---

### 해설
```python
binary = [1, 1, 1, 0, 1]
num = 0

for i in range(5):
    num = num * 2 + binary[i]

print(num)
```
```python
# 변수 선언 및 입력
binary = list(map(int, list(input())))
length = len(binary)

# 십진수로 변환합니다.
num = 0
for i in range(length):
    num = num * 2 + binary[i]

# 출력
print(num)
```