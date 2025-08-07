def is_valid_pos(board, row, col):
    # 열
    for idx in range(row): # 현재 행까지만 조사
        if board[idx][col] == 1: # 퀸이 있는 경우
            return False

    # 왼쪽 대각선 위
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): # 현재 행까지만 조사
        if board[i][j] == 1: # 퀸이 있는 경우
            return False

    # 오른쪽 대각선 위
    for i, j in zip(range(row, -1, -1), range(col, n)): # 현재 행까지만 조사
        if board[i][j] == 1: # 퀸이 있는 경우
            return False

    return True


def n_queens(row, board):
    global cnt
    cnt += 1

    # 종료 조건
    if row == n: # 모든 행에 대해 조사한 경우
        solutions.append([r[:] for r in board])
        return

    # 탐색
    for col in range(n):
        if is_valid_pos(board, row, col):
            board[row][col] = 1
            n_queens(row+1, board)
            board[row][col] = 0 # 백트래킹


n = 4
board = [[0] * n for _ in range(n)]  # 4*4 2차원 배열 생성
solutions = []  # 모든 솔루션을 저장할 리스트
cnt = 0 # 전체 호출 횟수

n_queens(0, board)

for solution in solutions:
    print(solution)

print(cnt)