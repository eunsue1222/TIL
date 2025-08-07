# import sys
# sys.stdin = open('sample_input.txt', 'r')

import heapq

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cmd = [list(map(int, input().split())) for _ in range(N)]
    result = []

    # 최대 힙
    max_heap = []

    # 연산
    for i in range(N):
        if cmd[i][0] == 1:
            heapq.heappush(max_heap, -cmd[i][1])
        elif cmd[i][0] == 2:
            if len(max_heap) != 0:
                largest = -heapq.heappop(max_heap)
                result.append(str(largest))
            else:
                result.append('-1')

    print(f'#{test_case} {" ".join(result)}')