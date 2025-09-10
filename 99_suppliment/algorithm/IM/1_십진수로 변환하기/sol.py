binary = input()

result = 0
for i in range(len(binary)):
    result += 2 ** i * int(binary[len(binary)-1-i])

print(result)