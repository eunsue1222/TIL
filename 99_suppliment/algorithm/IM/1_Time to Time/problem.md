## Time to Time

---

### 문제
2011년 11월 11일 A시 B분에서 시작하여 2011년 11월 11일 C시 D분까지 몇 분이 걸리는지를 계산하는 프로그램을 작성해보세요.

#### 입력
```
첫 번째 줄에 A, B, C, D가 공백을 사이에 두고 주어집니다.
```
```
ex) 2 5 4 1
```

#### 출력
```
첫 번째 줄에 해당하는 값을 출력합니다.
```
```
ex) 116
```

#### 제한 조건
```
0 <= A, C <= 23
0 <= B, D <= 59
모순된 경우는 주어지지 않는다고 가정해도 좋습니다.
```

#### 제한
```
Time Limit: 1000 ms
Memory Limit: 80 MiB
```
---

### 해설
```python
hour, mins = 2, 5
elapsed_time = 0

while True:
    if hour == 4 and mins == 1:
        break

    elapsed_time += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins = 0

print(elapsed_time)
```
```python
# 변수 선언 및 입력
a, b, c, d = tuple(map(int, input().split()))

# 출력
print((c * 60 + d) - (a * 60 + b))
```