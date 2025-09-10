N = int(input())

result = ''
while True:
    if N < 2:
        result += str(N)
        break

    result += str(N % 2)
    N //= 2

result = result[::-1]
print(result)