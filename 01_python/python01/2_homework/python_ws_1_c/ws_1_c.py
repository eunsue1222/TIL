# 3x3 크기의 2차원 리스트를 생성하여 초기 좌석 배치를 표현하시오. 좌석은 'O'로 표시합니다.
# (0,2), (1,0), (1,2), (2,0), (2,2) 좌석을 예매 처리하시오. 예매된 좌석은 'X'로 표시합니다.
# 예매된 좌석을 포함하여 현재 좌석 배치를 출력하시오.

# 아래에 코드를 작성하시오.
seats = [['O' for _ in range(3)] for _ in range(3)]

reserved = [(0,2), (1,0), (1,2), (2,0), (2,2)]
for row, col in reserved:
    seats[row][col] = 'X'

print('현재 좌석 배치:')
for row in seats:
    print(' '.join(row))