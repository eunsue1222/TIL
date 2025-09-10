A, B, C, D = map(int, input().split())

hour = C - A + ((B + D) // 60)
minute = (B + D) % 60
print(hour, minute)