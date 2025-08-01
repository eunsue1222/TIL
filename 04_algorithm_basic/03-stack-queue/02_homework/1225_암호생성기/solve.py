# import sys
# sys.stdin = open('input.txt', 'r')

from collections import deque

T = 10
for _ in range(T):
    test_case = int(input()) # 테스트케이스 번호
    data = list(map(int, input().split())) # 8개의 숫자 데이터
    queue = deque(data)

    while True:
        for count in range(1, 6): # 사이클: 1~5 감소
            element = queue.popleft() # 가장 왼쪽 요소 pop
            new_element = element - count # 숫자 감소
            if new_element <= 0: # 프로그램 종료 조건
                queue.append(0)
                break
            else: # 가장 오른쪽에 append
                queue.append(new_element)
        if new_element <= 0:
            break

    result = ' '.join(map(str, queue))
    print(f'#{test_case} {result}')