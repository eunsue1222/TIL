import sys
sys.stdin = open('input.txt')

'''
    입력
    재료의 수 N, 제한 칼로리 L(1 ≤ N ≤ 20, 1 ≤ L ≤ 104)
    점수 Ti, 칼로리 Ki(1 ≤ Ti ≤ 103, 1 ≤ Ki ≤ 103)
    
    출력
    제한 칼로리 이하의 조합 중, 가장 높은 점수
'''

def power_set(idx, acc_score, acc_kcal, sub_set):
    global result
    if acc_kcal > L:    # 제한 칼로리 초과시 조사 정지
        return

    # 아직 제한 칼로리를 넘기지 않았다면,
    # solve 영역에서 return 할 수 없음.
    if result < acc_score:  # 최대 점수 갱신
        result = acc_score  # 단, 점수가 더 높아질 수 있으므로 조사를 종료하지 않음.

    for i in range(idx, N):
        power_set(i + 1, acc_score + data[i][0], acc_kcal + data[i][1], sub_set + [data[i]])


# def power_set(idx, acc_score, acc_kcal):
#     global result
#     if acc_kcal > L:    # 제한 칼로리 초과시 조사 정지
#         return
#
#     # 아직 제한 칼로리를 넘기지 않았다면,
#     # solve 영역에서 return 할 수 없음.
#     if idx == N:
#         if result < acc_score:  # 최대 점수 갱신
#             result = acc_score  # 단, 점수가 더 높아질 수 있으므로 조사를 종료하지 않음.
#
#     power_set(idx + 1, acc_score + data[idx][0], acc_kcal + data[idx][1])
#     power_set(idx + 1, acc_score, acc_kcal)


T = int(input())
for tc in range(1, T + 1):
    # 재료수, 제한 칼로리
    N, L = map(int, input().split())
    # 점수, 칼로리
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    power_set(0, 0, 0, [])
    print(f'#{tc} {result}')
