import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 명령 개수 입력

    # 10x10 크기의 2차원 배열(행렬) 생성 및 0으로 초기화
    matrix = [[0 for _ in range(10)] for _ in range(10)]
    # 아래와 같은 방법은 잘못된 결과가 나올 수 있으니 주의:
    # 복사 이슈
    # matrix = [[0]*10]*10

    result = 0  # 최종 결과(값이 3이 되는 칸 수) 초기화

    for _ in range(N):
        r1, c1, r2, c2, c = map(int, input().split())  # 명령 입력 받기
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                # 왜 값만 더해도 될까?
                # → 그 칸에 빨강/파랑 등 명령값 c를 계속 더하면
                #    겹치는 곳은 누적합이 됨.
                #    (예: 빨강+파랑 = 1+2 = 3)
                matrix[x][y] += c     # 해당 칸에 값 더해주기

                if matrix[x][y] == 3: # 만약 합이 3이 되는 순간
                    result += 1       # 결과 카운트 증가

    # 각 행을 출력 (디버깅용)
    for i in range(10):
        print(matrix[i])

    print(f'#{tc} {result}')
