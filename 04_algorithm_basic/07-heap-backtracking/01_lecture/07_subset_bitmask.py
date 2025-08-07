nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 10
result = []
n = len(nums)

for i in range(1 << n): # 0 ~ 2^n-1
    current_subset = []
    current_sum = 0
    for j in range(n): # 0 ~ n-1
        if i & (1 << j): # 1 << j: 숫자 1을 왼쪽으로 j번 시프트
            current_subset.append(nums[j])
            current_sum += nums[j]
        if current_sum > target_sum:
            break
    if current_sum == target_sum:
        result.append((current_subset))
print(result)