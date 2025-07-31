def perm(selected, remain): # selected: 선택된 값 목록, reamin: 선택되지 않고 남은 값 목록
    if not remain: # 남은 값이 없는 경우
        print(*selected)
    else: # 남은 값이 있는 경우
        for idx in range(len(remain)): # 남아 있는 값 순회하기
            select_item = remain[idx] # idx번째 요소 선택
            remain_list = remain[:idx] + remain[idx+1:] # 선택된 idx번째 이외의 나머지 요소
            perm(selected + [select_item], remain_list)

perm([], [1, 2, 3])