import sys
sys.stdin = open('input.txt')

def selection_sort():
    # 첫 10개 요소만 특별한 정렬 수행
    for x in range(10):
        mIdx = x  # 현재 위치를 최적값으로 가정
        
        # 현재 위치 이후의 요소들 중에서 최적값 찾기
        for y in range(x + 1, N):
            # 홀수 인덱스: 최소값 선택
            if x % 2:
                if arr[mIdx] > arr[y]:
                    mIdx = y
            # 짝수 인덱스: 최대값 선택
            else:
                if arr[mIdx] < arr[y]:
                    mIdx = y
        
        # 현재 위치와 찾은 최적값 교환
        arr[x], arr[mIdx] = arr[mIdx], arr[x]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    selection_sort()
    result = ' '.join(map(str, arr[:10]))
    print(f'#{tc} {result}')