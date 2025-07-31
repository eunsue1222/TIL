def perm_no_slice(arr, start_idx):
    '''
    Args:
        arr: 순열을 만들 원본 리스트 (여기서는 변경 가능)
        start_idx: 현재 순열을 만들고 있는 시작 인덱스
    '''
    if start_idx == len(arr): # 시작 인덱스 = 마지막 인덱스 이면 끝
        print(arr)
        return

    for idx in range(start_idx, len(arr)):
        arr[start_idx], arr[idx] = arr[idx], arr[start_idx] # swap
        print(f'스왑된 배열 상태: {arr}')
        print(f'이번에 선택한 요소: {arr[start_idx]}')
        print(f'위치가 바뀐 요소: {arr[idx]}')
        perm_no_slice(arr, start_idx+1)
        arr[start_idx], arr[idx] = arr[idx], arr[start_idx] # swap
        print('=== 재귀 호출 후 돌아온 시점 ===')
        print(f'복원된 배열 상태: {arr}')

# 사용 예시
my_list = [1, 2, 3]
perm_no_slice(my_list, 0)