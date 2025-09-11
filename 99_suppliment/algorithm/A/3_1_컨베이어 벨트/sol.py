N, T = map(int, input().split())

upper_nums = list(map(int, input().split()))
lower_nums = list(map(int, input().split()))
arr = upper_nums + lower_nums

result = arr[N*2-T:] + arr[:N*2-T]
print(*result[:N])
print(*result[N:])