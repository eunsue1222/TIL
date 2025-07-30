# 팩토리얼을 반복문으로 구현

answer = 1
N = 5

for num in range(1, N+1):
    answer *= num # 1 * 2 *...* N
print(answer)