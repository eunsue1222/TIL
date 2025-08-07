import sys
sys.stdin = open('input.txt')

'''
    미래에 배울 내용 DP
    동적 계획 법중 bottom-up (for문) 방식에 테이블화 (tabulation) 을 적용하여 해결
    뭔가 엄청 어려운 말들인 것 같지만
    그냥 for문으로 이전에 계산 했던 값들일 list에 채워 나가면서 해결한다는 뜻.
    자세한 내용은 DP 수업에서...
'''
T = int(input())
for tc in range(1, T + 1):
    # 재료수, 제한 칼로리
    N, L = map(int, input().split())
    # 점수, 칼로리
    data = [list(map(int, input().split())) for _ in range(N)]

    '''
        제한 칼로리 이하 경우의 수에 대해 만들어 질 수 있는 최대 점수를 기록
        재료1의 칼로리 10, 점수 1
        재료2의 칼로리 11, 점수 2
        이때, 칼로리 21로 만들 수 있는 점수 3
        -> 기존에 21 칼로리로 만들 수 있는 점수와 지금 만든 점수의 최댓값
        -> table[21] = max(table[21], 1+2)
        
        재료3의 칼로리 8, 점수 100
        재료4의 칼로리 13, 점수 100
        -> 기존에 21 칼로리로 만들 수 있는 점수와 지금 만든 점수의 최댓값
        -> table[21] = max(table[21], 100 + 100)
    '''
    table = [0] * (L + 1)
    for score, kcal in data:                # 모든 정보에 대해
        for i in range(L, kcal - 1, -1):    # 제한 칼로리부터, 현재 칼로리 범위까지
            '''
                제한 칼로리가 100
                재료 5의 칼로리가 10이라면,
                
                table의 0부터 9까지는 무슨 짓을해도, 재료 1을 더한 점수를 구할 수 없음.
                table의 최대 크기는 제한 칼로리 100 까지 있음.
                10 부터 100까지 모든 경우에 대해서 점수 만큼 값을 더하고 최댓값으로 갱신
            '''
            table[i] = max(table[i], table[i - kcal] + score)
    print(table)
    print(f'#{tc}', table[L])