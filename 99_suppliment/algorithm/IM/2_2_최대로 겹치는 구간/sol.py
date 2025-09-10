N = int(input())

lines = [0] * 201
offset = 100

for _ in range(N):
    x1, x2 = map(int, input().split())
    for i in range(x1+offset, x2+offset+1):
        lines[i] += 1

print(lines)
result = max(lines) if max(lines) != 1 else 0
print(result)