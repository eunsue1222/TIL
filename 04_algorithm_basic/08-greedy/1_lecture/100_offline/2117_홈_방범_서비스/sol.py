import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    house = []
    result = 0

    # 모든 집들의 좌표를 house 리스트에 저장합니다.
    for r in range(N):
        for c in range(N):
            if data[r][c] == 1:
                house.append((r, c))

    # 모든 좌표를 돌며 검토합니다.
    for r in range(N):
        for c in range(N):
            # 해당 좌표에서 집까지의 맨해튼 거리 + 1을 계산하여 distance 리스트에 저장합니다.
            distance = []
            for (y, x) in house:
                distance.append(abs(r-y) + abs(c-x) + 1)
            # 계산된 거리 중 가장 먼 거리부터 내림차순으로 검토합니다.
            K = max(distance)
            for k in range(K, 0, -1):
                cnt = 0
                for d in distance:
                    if d <= k:
                        cnt += 1
                # cnt를 기준으로 이윤을 계산하여 0보다 크거나 같다면 result를 갱신합니다.
                if (cnt * M) - (k * 2 * (k - 1) + 1) >= 0:
                    result = max(cnt, result)
                    break

    print(f'#{tc} {result}')