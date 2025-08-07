import sys
sys.stdin = open("input.txt", "r")

from collections import deque
import heapq


def start_parking(n, costs, weights, entry_order):
    """
    주차장 시뮬레이션을 실행하여 총 수입을 계산한다.
    
    Args:
        n: 주차 공간 수
        costs: 각 주차 공간의 단위 무게당 요금
        weights: 각 자동차의 무게
        entry_order: 입/출차 순서 (양수: 입차, 음수: 출차)
    
    Returns:
        int: 총 수입
    """
    # 초기화
    total_income = 0
    waiting_queue = deque()  # 주차 대기 큐
    free_spaces = list(range(n))  # 사용 가능한 주차 공간 (번호가 작은 순서로 우선순위)
    heapq.heapify(free_spaces)
    car_positions = {}  # 차량별 주차 위치 추적

    # 입/출차 처리
    for entry_car in entry_order:
        if entry_car > 0:  # 입차
            car_number = entry_car - 1
            
            if free_spaces:  # 주차 공간이 있는 경우
                space_index = heapq.heappop(free_spaces)
                car_positions[car_number] = space_index
                total_income += costs[space_index] * weights[car_number]
            else:  # 주차 공간이 꽉 찬 경우
                waiting_queue.append(car_number)
                
        else:  # 출차
            car_number = (-entry_car) - 1
            space_index = car_positions[car_number]
            heapq.heappush(free_spaces, space_index)
            
            # 대기 중인 차량이 있으면 바로 주차
            if waiting_queue:
                waiting_car = waiting_queue.popleft()
                space_index = heapq.heappop(free_spaces)
                car_positions[waiting_car] = space_index
                total_income += costs[space_index] * weights[waiting_car]

    return total_income

T = int(input().strip())

for t in range(1, T + 1):
    n, m = map(int, input().split())  # 주차공간 수, 자동차 수
    costs = [int(input()) for _ in range(n)]  # 주차 공간별 단위 무게당 요금
    weights = [int(input()) for _ in range(m)]  # 자동차별 무게
    entry_order = [int(input()) for _ in range(2 * m)]  # 입/출차 순서
    
    result = start_parking(n, costs, weights, entry_order)
    print(f"#{t} {result}")























