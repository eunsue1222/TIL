A, B, C, D = map(int, input().split())

hour = C - A
minute = D - B

if minute < 0:
    minute += 60
    hour -= 1

if hour < 0:
    hour += 24

result = hour * 60 + minute
print(result)