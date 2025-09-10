## 블럭쌓는 명령

---

### 문제
1번 칸부터 N번째 칸까지 순서대로 총 N개의 칸이 있습니다. 이 중 Ai번째 칸부터 Bi번째 칸까지 각각 블럭을 1씩 쌓으라는 명령이 총 K번 주어집니다. (1 <= i <= K)

명령을 다 수행한 이후 1번 칸부터 N번 칸까지 쌓인 블럭의 수 중 최댓값을 출력하는 프로그램을 작성해보세요.

#### 입력
```
첫 번째 줄에 N과 K가 공백을 사이에 두고 주어집니다.
두 번째 줄부터 K개의 줄에 걸쳐 i = 1부터 i = k까지 순서대로 Ai번째 칸부터 Bi번째 칸까지 블럭을 각각 1개씩 쌓으라는 명령이 한 줄에 하나씩 주어집니다.
```
```
ex) 
7 4
5 5
2 4
4 6
3 5
```

#### 출력
```
첫 번째 줄에 각 칸에 있는 블럭의 수 중 최댓값을 출력합니다.
```
```
ex) 
3
```

#### 제한 조건
```
1 <= N <= 100
1 <= K <= 100
1 <= Ai <= Bi <= N
```

#### 제한
```
Time Limit: 1000 ms
Memory Limit: 80 MiB
```
---

### 해설
```python
# 변수 선언 및 입력
n, k = tuple(map(int, input().split()))
segments = [
    tuple(map(int, input().split()))
    for _ in range(k)
]

blocks = [0] * (n + 1)

# 블럭을 특정 구간에 쌓아줍니다.
for a, b in segments:
    for i in range(a, b + 1):
        blocks[i] += 1

# 최댓값을 구합니다.
max_num = max(blocks)
print(max_num)
```