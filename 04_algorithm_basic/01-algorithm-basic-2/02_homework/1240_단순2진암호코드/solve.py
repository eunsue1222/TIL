# import sys
# sys.stdin = open('input.txt', 'r')

code = {0:'0001101', 1:'0011001', 2:'0010011', 3:'0111101', 4:'0100011', 5:'0110001', 6:'0101111', 7:'0111011', 8:'0110111', 9:'0001011'}

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    array = [input().strip() for _ in range(N)]

    line = [row for row in array if '1' in row][0] # 암호코드가 들어있는 줄 추출
    valid = line[line.rfind('1')-55:line.rfind('1')+1] # 암호코드 추출

    decoded = []
    for i in range(len(valid)//7): # 암호코드 개수만큼 (8비트)
        num = valid[7*i:7*i+7] # 암호코드 1비트 -> 숫자 변환
        for key, value in code.items():
            if value == num:
                decoded.append(key)

    even_idx = [decoded[idx] for idx in range(len(decoded)) if idx%2 == 0] # 짝수 인덱스 요소
    odd_idx = [decoded[idx] for idx in range(len(decoded)) if idx%2 != 0] # 홀수 인덱스 요소
    
    # 유효 코드 검사:  (홀수 자리의 합 x 3) + (짝수 자리의 합) = 10의 배수
    if (sum(even_idx)*3 + sum(odd_idx)) % 10 == 0:
        result = sum(decoded)
    else:
        result = 0

    print(f'#{test_case} {result}')