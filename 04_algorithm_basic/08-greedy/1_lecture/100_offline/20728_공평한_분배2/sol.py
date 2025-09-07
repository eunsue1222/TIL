import sys
sys.stdin = open('input.txt')

T = int(input())


"""
이 문제는 조합적으로 접근하면 O(nCk) 시간복잡도 , 조합을 구해야 하기 떄문에 
근데 N이 50까지 주어지기 때문에, 일반적으로 k가 n의 절반일 떄 가장 크므로 
50C25 => 10^15승 = 1,000 조 ( 불가능 ) => 다른 방법을 찾아보자 
"""
T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))

    """
    정렬하는 이유 
    - 정렬을 하면 어떤 시작점으로 하든 연속적으로 K개를 선택하면 가장 앞쪽에는 최소값, 가장 뒷쪽에는 최대값이 정렬됨 
    """
    data.sort()  # 주머니 속 사탕의 개수를 오름차순으로 정렬
    result = float('inf')  # 최소 차이를 무한대로 초기화

    # 이미 정렬이 되어있기 때문에, 처음부터 K개씩 고르는 방식으로 전체 사탕 리스트를 순회한다.
    # 이 때, K개씩 접근하기 때문에 그 전까지만 순회해야한다.
    for i in range(N - K + 1):
        # 현재 구간의 최대값(i+K-1)과 최소값(i)의 차이 계산
        # 맨 앞은 최소값, 맨 뒤는 최대값 , 가운데는 알 필요없다 ( 이유는 이미 오름차순 정렬이 되어 있기 때문에 )
        current_diff = data[i + K - 1] - data[i]
        # 현재 차이가 지금까지의 최소 차이보다 작으면 갱신
        if current_diff < result:
            result = current_diff

    print(f"#{t} {result}")