import sys

sys.stdin = open('input.txt') # open을 사용해서 input 파일을 연다

for _ in range(10):
    # 입력 받은 문자열을 공백 기준으로 쪼개서 정수로 바꾼다음 리스트에 담는걸 100번 반복
    tc = input() # 테스트케이스 번호 입력    
    # data = []
    # for _ in range(100):
    #     tmp_list = input().split()
    #     map_data = map(int, tmp_list)
    #     map_to_list_data = list(map_data)
    #     data.append(map_to_list_data)
    # print(data)
    data = [list(map(int, input().split())) for _ in range(100)]
    print(data)
    
    # 각 행마다 가진 값들을 더한다.
    # 각 열마다 가진 값들을 더한다.
    # 대각선의 값들을 더한다.
    # 그 모든 값들 중 제일 큰 값을 구한다. -> max 금지