def comb(arr, n):
   result = []

   if n == 1: # 선택할 요소가 1개인 경우
      return [[i] for i in arr]

   for idx in range(len(arr)): # 요소 순회하기
      select_item = arr[idx]
      for rest in comb(arr[idx+1:], n-1): # 나머지 요소들로 재귀호출하여 조합을 다시 구성
         result.append([select_item] + rest)
   return result

print(comb([1, 2, 3, 4], 3))  # [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4] 출력
