def find_subset(start, current_subset, current_sum):
    # 가지 치기
    if current_sum > target_sum:
        return

    # 종료 조건
    if current_sum == target_sum:
        result.append(list(current_subset))
        return

    # 탐색
    for idx in range(start, len(nums)):
        num = nums[idx]
        current_subset.append(num)
        find_subset(idx+1, current_subset, current_sum+num)
        current_subset.pop()


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 10
result = []

find_subset(start=0, current_subset=[], current_sum=0)
print(result)