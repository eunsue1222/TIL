T = int(input())
for test_case in range(1, T+1):
    number, exchange = map(int, input().split())

    # 뒤에서부터 오면서 가장 큰수
    for num in range(9, -1, -1):
        big_index = str(number).rfind(str(num))
        print(big_index)

    # 앞에서부터 오면서 가장 작은수
    # 바꾸기

    # print(f'#{test_case} {}')