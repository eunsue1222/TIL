# import sys
# sys.stdin = open('sample_input.txt')

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end

    while True:
        while left <= end and arr[left] < pivot:
            left += 1
        while right > start and arr[right] >= pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break

    arr[start], arr[right] = arr[right], arr[start]

    return right

def quick_sort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        quick_sort(arr, start, p-1)
        quick_sort(arr, p+1, end)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    quick_sort(numbers, 0, len(numbers)-1)
    print(f'#{test_case} {numbers[N//2]}')