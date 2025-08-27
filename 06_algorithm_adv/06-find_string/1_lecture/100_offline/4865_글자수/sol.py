import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    print(f'#{tc} {max(map(lambda x: str2.count(x), str1))}')