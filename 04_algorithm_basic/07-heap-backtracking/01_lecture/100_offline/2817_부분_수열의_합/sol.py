'''
A1, A2, ... , AN의 N개의 자연수가 주어졌을 때, 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수를 구하는 프로그램을 작성하시오.

[출력]

각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 부분 수열의 합이 K가 되는 경우의 수를 출력한다.
'''
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 원소의 개수(20), K: 목표 합 (1 이상)
    N, K = map(int, input().split())
    # N개의 정수 (1 <= An <= 100)
    data = list(map(int, input().split()))
    result = 0
    '''
        N이 최대 20 -> 2**N ≈ 10**6 (1048576)
        + 여기에 N개의 요소를 선택할 지 모든 경우의 수에 대해 조회 -> 2**N * N ≈ 10**6 * 20 
        + 부분집합을 리스트로 만들어 sum 함수 호출 -> (2**N * N * K) ≈ 10**6 * 40?
            -> 10**6 * 40 -> 4 * 10**7 (40000000 약 4천만회) * TC (내부 TC에 따라 다름)
                  
        -> 부분 집합의 합을 리스트가 아니라 일반 정수로 처리하자. O(1)
        정수 연산 -> 2 * 10**7 (20000000 약 2천만회) * TC (내부 TC에 따라 다름)
        
        단, 두 경우에 대해서 Big O를 묻는다면 둘 다, 주 지배항인
        O(2**N) 으로만 표기. 2**N (* N <- 의미 없음.) (* K <- 의미 없음)
        
    '''
    for i in range(1, 1 << N):      # 목표 1이상: 공집합 없음.
        # temp = 0
        temp_list = []
        for j in range(N):          # 모든 원소에 대해
            if i & (1 << j):        # j번째 원소가 i번째 경우의 수에 포함될 것인지 판별
                # temp += data[j]
                temp_list.append(data[j])
        # print(temp_list)
        # if temp == K:          # 부분 집합의 합이 K라면
        #     result += 1             # 만들 수 있음
        if sum(temp_list) == K:
            result += 1
    print(f'#{tc} {result}')

