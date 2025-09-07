import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 신청서 수
    SE = [list(map(int, input().split())) for _ in range(N)]  # 시작시간, 종료시간

    SE.sort(key=lambda x: x[1])  # 종료시간 기준으로 정렬

    result = 1  # 첫번째 화물차는 무조건 배정
    end_time = SE[0][1]  # 첫번째 화물차의 종료시간 저장

    for i in range(1, N):  # 두번째 화물차부터 반복
        if SE[i][0] >= end_time:  # 시작시간이 종료시간보다 크거나 같으면, (앞 작업 종료와 동시에 시작 가능)
            result += 1  # 배정
            end_time = SE[i][1]   # 종료시간 갱신
    print(f'#{tc} {result}')