import sys
sys.stdin = open('input.txt')

def merge_arr(left_arr, right_arr):
    global result
    # 왼쪽 배열의 마지막 요소가 오른쪽 배열의 마지막 요소보다 큰 경우 카운트 증가
    if left_arr[-1] > right_arr[-1]:
        result += 1
    
    merge_arr = []  # 병합된 결과를 저장할 리스트
    left_idx, right_idx = 0, 0  # 각 배열의 인덱스 포인터
    n, m = len(left_arr), len(right_arr)  # 각 배열의 길이

    # 두 배열을 순서대로 비교하여 병합
    while left_idx != n and right_idx != m:
        # 왼쪽 배열의 현재 요소가 오른쪽 배열의 현재 요소보다 작거나 같은 경우
        if left_arr[left_idx] <= right_arr[right_idx]:
            merge_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            merge_arr.append(right_arr[right_idx])
            right_idx += 1

    # 남은 요소들을 결과에 추가
    merge_arr += left_arr[left_idx:]
    merge_arr += right_arr[right_idx:]

    return merge_arr


def divide_arr(a):
    # 배열의 길이가 1인 경우, 더 이상 나눌 수 없으므로 반환
    if len(a) == 1:
        return a
    
    # 배열을 반으로 나누어 분할 정복
    mid = len(a) // 2
    left = divide_arr(a[:mid])    # 왼쪽 절반을 재귀적으로 분할
    right = divide_arr(a[mid:])   # 오른쪽 절반을 재귀적으로 분할
    
    # 분할된 배열들을 병합하여 반환
    return merge_arr(left, right)


T = int(input())  # 테스트 케이스의 수

for tc in range(1, T + 1):
    N = int(input())  # 배열의 크기
    arr = list(map(int, input().split()))  # 배열 요소
    result = 0  # 왼쪽 배열의 마지막 요소가 오른쪽보다 큰 경우를 세는 변수
    
    arr = divide_arr(arr)  # 배열 분할 및 병합 정렬 수행
    median = arr[N // 2]  # 정렬된 배열의 중앙값
    print(f'#{tc} {median} {result}')  # 결과 출력