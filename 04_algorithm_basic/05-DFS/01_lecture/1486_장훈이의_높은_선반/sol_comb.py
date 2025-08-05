import sys
sys.stdin = open('input.txt')

def combination(arr, r): # r: 선택할 요소의 개수
    result = []

    if r == 1:
        return [[i] for i in arr] # 각 값들을 배열로 반환

    for idx in range(len(arr)): # 조합
        element = arr[idx]
        for rest in combination(arr[idx+1:], r-1):
            result.append([element] + rest)

    return result


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    data = list(map(int, input().split()))

    min_height = 10000 * N # 직원당 최대 키 * 최대 직원수

    for r in range(1, N+1):
        for comb in combination(data, r): # 조합을 통해 얻어낸 리스트 순회
            total = sum(comb) # 조합에 들어온 모든 점원들의 키의 합
            if total >= B:
                min_height = min(min_height, total)

    print(f'#{tc} {min_height - B}')