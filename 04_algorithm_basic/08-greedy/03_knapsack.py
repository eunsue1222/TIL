def fractional_knapsack_greedy(capacity, items):
    items.sort(key=lambda x: x[1] / x[0], reverse=True) # 무게 당 가격으로 오름차순 정렬

    result = 0
    remain_capacity = capacity

    for weight, value in items:
        if remain_capacity <= 0:
            break

        if remain_capacity >= weight: # 통째로 넣을 수 있는 경우
            result += value
        else: # 나눠서 넣어야 하는 경우
            fraction = remain_capacity / weight
            result += value * fraction
            remain_capacity = 0

    return result


capacity = 30  # 배낭의 최대 무게
items = [(5, 50), (10, 60), (20, 140)] # (무게, 가치)
result = fractional_knapsack_greedy(capacity, items)
print(f"최대 가치: {result}")