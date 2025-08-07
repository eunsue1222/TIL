# import sys
# sys.stdin = open('sample_input.txt', 'r')

def backtrack(depth, current, total):
    global minimum_usage

    # 가지 치기
    if total >= minimum_usage:
        return

    # 종료 조건
    if depth == N-1: # N-1개 구역 방문 완료
        total += table[current][0] # 도착점: 다시 사무실로 돌아가기
        minimum_usage = min(minimum_usage, total)
        return

    # 탐색
    for next in range(1, N): # 사무실 제외하고 방문하기
        if not visited[next]: # 방문 확인
            visited[next] = True
            backtrack(depth+1, next, total+table[current][next]) # 다음 구역으로 이동
            visited[next] = False # 백트래킹


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)] # 0: 사무실, 1 ~ M-1: 관리구역

    visited = [False] * N # 방문 여부 체크
    minimum_usage = float('inf') # 최소 배터리 사용량

    visited[0] = True # 출발점: 사무실에서 출발하기
    backtrack(0, 0, 0) # 중복 x, 순열

    print(f'#{test_case} {minimum_usage}')