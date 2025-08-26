import sys
sys.stdin = open('input.txt')


def quicksort(arr):
    global cnt
    cnt += 1  # 퀵소트 호출 횟수 카운트
    
    # 배열 길이가 2 미만인 경우, 정렬할 필요 없음
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]  # 배열의 마지막 요소를 피벗으로 선택
        smaller, equal, larger = [], [], []  # 피벗보다 작은, 같은, 큰 요소들을 저장할 리스트
        
        # 배열의 모든 요소를 피벗과 비교하여 분류
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        
        # 재귀적으로 작은 부분과 큰 부분을 정렬한 후 합치기
        return quicksort(smaller) + equal + quicksort(larger)


T = int(input())  # 테스트 케이스의 수

for tc in range(1, T+1):
    cnt = 0  # 퀵소트 호출 횟수 초기화
    n = int(input())  # 배열의 크기
    unsorted_list = list(map(int, input().split()))  # 정렬할 배열
    
    result = quicksort(unsorted_list)  # 퀵소트 수행
    # print(result)  # 전체 정렬 결과 (주석 처리됨)
    print(f'#{tc} {result[n//2]}')  # 중앙값 출력