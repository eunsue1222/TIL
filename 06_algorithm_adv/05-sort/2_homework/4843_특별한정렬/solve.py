# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    result = []
    for i in range(N):
        smallest = float('inf')
        biggest = float('-inf')

        if i % 2 != 0:
            for j in range(len(numbers)):
                if numbers[j] < smallest:
                    smallest = numbers[j]
            result.append(numbers.pop(numbers.index(smallest)))
        else:
            for j in range(len(numbers)):
                if numbers[j] > biggest:
                    biggest = numbers[j]
            result.append(numbers.pop(numbers.index(biggest)))

    print(f"#{test_case} {' '.join(map(str, result[:10]))}")