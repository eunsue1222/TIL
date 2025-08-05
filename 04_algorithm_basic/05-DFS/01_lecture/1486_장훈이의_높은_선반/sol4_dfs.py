import sys
sys.stdin = open("input.txt")

def dfs(idx, total): # 현재 탐색 중인 점원
    global min_height

    # 가지 치기
    if total >= min_height:
        return

    # 종료 조건
    if idx == N:
        if total >= B:
            min_height = min(min_height, total)
        return

    # 탐색
    dfs(idx+1, total+arr[idx]) # 선택 o
    dfs(idx+1, total) # 선택 x


T = int(input())
for tc in range(1, T + 1):
    # N: 사람 수, B: 목표 높이
    N, B = map(int, input().split())
    # 각 사람의 키를 입력 받아 리스트로 저장
    arr = list(map(int, input().split()))

    # 직원당 키는 최대 10000이므로, 최대 높이는 10000 * N
    min_height = 10000 * N 

    dfs(0, 0)

    # 목표 높이 B를 빼서 실제로 초과된 부분만 출력
    print(f"#{tc} {min_height - B}")

