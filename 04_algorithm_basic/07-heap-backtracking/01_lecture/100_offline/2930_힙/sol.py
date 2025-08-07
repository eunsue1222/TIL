import sys
sys.stdin = open('input.txt')

'''
    초기에 최대 힙이 비어있을 때에 다음의 2가지 연산을 수행하는 프로그램을 작성하자.
    
    연산 1. 자연수 x를 삽입
    연산 2. 최대 힙의 루트 노드의 키값을 출력하고, 해당 노드를 삭제
    
    입력
    각 테스트 케이스마다 첫째 줄에 수행해야하는 연산의 수를 나타내는 자연수 N(1≤N≤105)이 주어진다. 
    둘째 줄부터 N개의 줄에 걸쳐서 순서대로 수행해야하는 연산에 대한 정보가 주어진다.
    
    출력
    연산 2의 결과들을 공백 하나를 사이에 두고 순서대로 출력한다.
    만약, 연산 2를 수행해야 하는데 힙에 원소가 없어서 출력해야 할 최대 키값이 존재하지 않는다면 -1을 출력한다. 
'''
import heapq

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 1 1: 1을 삽입, 2: 루트 노드 값을 제거
    data = [list(map(int, input().split())) for _ in range(N)]
    arr = []        # heap으로 사용할 배열
    result = []     # heappop 한 결과를 담을 배열
    for item in data:   # 전체 정보에 대해서 순회
        # print(arr)
        # print(heapq.nlargest(2, arr))
        # print()
        if len(item) == 2:      # len == 2: 삽입정보, 삽입할 아이템
            heapq.heappush(arr, -item[1])       # 최대 힙을 위해 부호 치환 후 삽입
        elif heapq.nlargest(1, arr):            # 힙의 최대값이 1개 이상 있다면
            result.append(-heapq.heappop(arr))  # pop하면서 다시 부호 정상화
        else:
            result.append(-1)   # pop할 값이 없으면 -1
    print(f'#{tc}', *result)
