# import sys
# sys.stdin = open('input.txt', 'r')

T = 10
for _ in range(T):
    test_case = int(input()) # 테스트케이스 번호
    game = [list(map(int, input().split())) for _ in range(100)] # 100x100 맵 사다리 게임

    # 도착점 찾기
    for i in range(100):
        if game[99][i] == 2:
            x, y = 99, i
            break

    while x > 0:
        if y > 0 and game[x][y-1] == 1: # 왼쪽 이동 가능성
            while y > 0 and game[x][y-1] == 1:
                y -= 1 # 왼쪽 이동
            x -= 1 # 위쪽 이동
        elif y < 99 and game[x][y+1] == 1: # 오른쪽 이동 가능성
            while y < 99 and game[x][y+1] == 1:
                y += 1 # 오른쪽 이동
            x -= 1 # 위쪽 이동
        else:
            x -= 1 # 위쪽 이동

    print(f'#{test_case} {y}')