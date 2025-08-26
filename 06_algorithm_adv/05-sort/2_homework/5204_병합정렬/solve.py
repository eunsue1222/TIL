# import sys
# sys.stdin = open('sample_input.txt')

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr):
    global count
    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    if left[-1] > right[-1]:
        count += 1

    return merge(left, right)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    count = 0

    sorted_numbers = merge_sort(numbers)
    print(f'#{test_case} {sorted_numbers[N//2]} {count}')