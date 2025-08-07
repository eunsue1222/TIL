import sys
sys.stdin = open('test_input.txt')


def power_set(idx, acc):
    global cnt_for_power_set
    cnt_for_power_set += 1
    for i in range(idx, N):
        power_set(i + 1,  acc + data[i])

def solve_condition(idx, acc):
    global cnt_for_solve_condition
    cnt_for_solve_condition += 1
    if acc == K:
        return
    for i in range(idx, N):
        solve_condition(i + 1,  acc + data[i])

def prunning(idx, acc):
    global cnt_for_prunning
    cnt_for_prunning += 1
    if acc > K:
        return
    if acc == K:
        return
    for i in range(idx, N):
        prunning(i + 1,  acc + data[i])

def prunning_2(idx, acc):
    global cnt_for_prunning_2
    cnt_for_prunning_2 += 1
    if acc > K:
        return
    if idx == N:
        return
    if acc == K:
        return
    prunning_2(idx + 1,  acc + data[idx])
    prunning_2(idx + 1, acc)

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    cnt_for_power_set = 0
    cnt_for_solve_condition = 0
    cnt_for_prunning = 0
    cnt_for_prunning_2 = 0
    power_set(0, 0)
    solve_condition(0, 0)
    prunning(0, 0)
    prunning_2(0, 0)

    print(f'K == {K}')
    print(cnt_for_power_set, '모든 경우의 수')
    print(cnt_for_solve_condition, '문제 해결을 위한 조건')
    print(cnt_for_prunning, '가지치기')
    print(cnt_for_prunning_2, '가지치기 2')
    print()


