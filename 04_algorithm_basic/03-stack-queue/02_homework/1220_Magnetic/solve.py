import sys
sys.stdin = open('input.txt', 'r')

T = 10
for test_case in range(1, T+1):
    size = int(input())
    table = [list(map(str, input().split())) for _ in range(size)]

    count = 0
    for row in list(zip(*table)):
        print(row)