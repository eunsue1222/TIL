import sys
sys.stdin = open('input.txt')

'''
    DFS 방식의 조사에서도 big O는 O(2**N) or O(N * 2**N) 이다.
    그럼에도, 실행 시간의 차이는 어마어마 한데 왜 그럴까?
    prunning 조건인 K의 값에 따라서 불필요한 조사를 하지 않는 경우가 기하급수 적으로 커지기 때문이다.
    이 과정이 얼마나 차이나는지 보기 위해...
    comparison 참고.
'''
def power_set(idx, acc):        # 멱집합 생성
    global result
    if acc > K:
        '''
            목표치보다 커졌다? 이번 data에는 음수가 없다.
            K로 돌아 갈 수 있는 경우의 수가 존재 하지 않는다.
            더 이상 조사 할 의미 없음
        '''
        return
    if acc == K:       # 총합이 K라면
        # 이 문제 해결을 위한 solve 과정을 거치는 일
        result += 1                  # 경우의 수 1 증가
        return
    for i in range(idx, N):         # N개에 대해서 이전에 선택했던 값을 제외한 수들에 대해
        # 이번에 선택한 값 다음부터 연산을 진행
        # 이번에 선택한 값을 누적값에 더해서 다음 집합 생성
        power_set(i + 1,  acc + data[i])

T = int(input())

for tc in range(1, T + 1):
    # N: 원소의 개수(20), K: 목표 합 (1 이상)
    N, K = map(int, input().split())
    # N개의 정수 (1 <= An <= 100)
    data = list(map(int, input().split()))
    result = 0
    power_set(0, 0)    # 0번째 요소부터 조사
    print(f'#{tc} {result}')

