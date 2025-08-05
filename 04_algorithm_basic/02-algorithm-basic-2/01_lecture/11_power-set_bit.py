arr = [1, 2, 3]
n = len(arr)
subsets = []

# for idx in range(2**n):
for idx in range(1 << n):
    print(idx)
    tmp_subset = []
    for j in range(n):
        if idx & (1 << j):
            tmp_subset.append(arr[j])
    subsets.append(tmp_subset)

    # 추가 조건
    if sum(tmp_subset) == 3:
        subsets.append(tmp_subset)

print(subsets)