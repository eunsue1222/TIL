import sys
sys.stdin = open('input.txt')

def bubble_sort():
    # 배열의 길이만큼 반복
    for x in range(N):
        # 뒤에서부터 현재 위치까지 비교하면서 버블링
        for y in range(N-1, x, -1):
            # 홀수 인덱스: 오름차순 정렬 (작은 값이 앞으로)
            if x % 2:
                if arr[x] > arr[y]:
                    arr[x], arr[y] = arr[y], arr[x]
            # 짝수 인덱스: 내림차순 정렬 (큰 값이 앞으로)
            else:
                if arr[x] < arr[y]:
                    arr[x], arr[y] = arr[y], arr[x]
T = int(input())  # 테스트 케이스의 수

for tc in range(1, T+1):
    N = int(input())  # 배열의 크기
    arr = list(map(int, input().split()))  # 배열 요소

    bubble_sort()  # 특별한 버블 정렬 수행
    result = ' '.join(map(str, arr[:10]))  # 첫 10개 요소만 출력 형식으로 변환
    print(f'#{tc} {result}')  # 결과 출력