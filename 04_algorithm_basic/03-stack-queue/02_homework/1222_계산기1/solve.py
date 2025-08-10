# import sys
# sys.stdin = open('input.txt', 'r')

T = 10
for test_case in range(1, T+1):
    length = int(input())
    expression = list(input())

    total = 0
    for e in expression:
        if e.isdigit():
            total += int(e)

    print(f'#{test_case} {total}')