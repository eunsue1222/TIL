## 2진수로 변환하기

---

### 문제
십진수 N이 주어지면 0과 1로만 이루어진 2진수로 그 수를 변환하여 출력하는 프로그램을 작성해보세요.

#### 입력
```
첫 번째 줄에 정수 N이 주어집니다.
```
```
ex) 29
```

#### 출력
```
첫 번째 줄에 주어진 십진수를 2진수로 변환한 결과를 공백없이 출력합니다.
```
```
ex) 11101
```

#### 제한 조건
```
0 <= N <= 100000
```

#### 제한
```
Time Limit: 1000 ms
Memory Limit: 80 MiB
```
---

### 해설
```python
n = 29
digits = []

while True:
    if n < 2:
        digits.append(n)
        break

    digits.append(n % 2)
    n //= 2

# print binary number
for digit in digits[::-1]:
    print(digit, end="")
```
```python
# 변수 선언 및 입력
n = int(input())
digits = []

# 이진수로 변환합니다.
while True:
    if n < 2:
        digits.append(n)
        break

    digits.append(n % 2)
    n //= 2

# 이진수를 출력 합니다.
# 뒤집은 다음에 출력해야 함에 유의합니다.
for digit in digits[::-1]:
    print(digit, end="")
```