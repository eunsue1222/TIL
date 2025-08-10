# import sys
# sys.stdin = open('sample_input.txt', 'r')

from collections import deque

T = int(input())
for test_case in range(1, T+1):
    M, N = map(int, input().split()) # M: 화덕 크기, N: 피자 개수
    C = list(map(int, input().split())) # C: 피자 당 치즈의 양

    waiting_queue = deque() # 대기열
    waiting_queue.extend((idx+1, C[idx]) for idx in range(N)) # (피자 번호, 치즈 양)

    oven = deque() # 오븐
    for _ in range(M):
        oven.append(waiting_queue.popleft())

    # 피자 굽기
    while len(oven) > 1:
        pizza, cheese = oven.popleft()
        cheese //= 2
        if cheese > 0: # 피자 굽기 진행중
            oven.append((pizza, cheese))
        else: # 피자 굽기 완료
            if waiting_queue: # 대기열 존재
                oven.append(waiting_queue.popleft())

    print(f'#{test_case} {oven[0][0]}')