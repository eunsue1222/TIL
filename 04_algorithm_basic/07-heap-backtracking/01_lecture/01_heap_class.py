class MinHeap:
    def __init__(self):
        self.heap = []  # 힙을 저장할 빈 리스트 초기화
        self.length = 0  # 힙의 길이 초기화

    # 힙에 새로운 요소를 추가
    def heappush(self, item):
        self.heap.append(item)  # 새로운 요소를 리스트의 끝에 추가
        self.length += 1  # 힙의 길이 증가
        self._siftup(self.length-1) # 힙 속성 유지: 가장 마지막에 삽입된 요소의 index 전달

    # 힙에서 최소 요소를 제거하고 반환
    def heappop(self):
        if self.length == 0:
            raise IndexError("힙이 비었습니다.")  # 힙이 비어 있는 경우 예외 발생
        if self.length == 1:
            self.length -= 1
            return self.heap.pop()  # 힙에 요소가 하나만 있는 경우 그 요소를 반환

        root = self.heap[0] # 루트 노드의 요소 반환
        self.heap[0] = self.heap.pop() # 마지막 요소를 루트로 이동
        self.length -= 1 # 길이 감소
        self._siftdown(0) # 힙 속성 유지: 가장 처음에 삽입된 요소의 index 전달
        return root
        
    # 주어진 리스트을 힙으로 변환
    def heapify(self, array):
        self.heap = array[:]  # 리스트의 복사본을 힙으로 사용
        self.length = len(array)
        for i in range(self.length // 2 - 1, -1, -1): # 이진 트리이기 때문에
            self._siftdown(i)

    # 삽입 후 힙 속성을 유지하기 위해 사용되는 보조 메서드
    def _siftup(self, idx): # 내부적으로 사용할 메서드
        # 마지막에 삽입된 노드와 부모 노드의 크기를 비교
        parent = (idx - 1) // 2 # 부모 노드의 인덱스
        while idx > 0 and self.heap[idx] < self.heap[parent]: # 자식 노드 인덱스 <0 and  자식 노드 < 부모 노드
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx] # 자식 노드와 부모 노드 스왑
            parent = (idx - 1) // 2 # 부모 노드 갱신

    # 삭제 후 힙 속성을 유지하기 위해 사용되는 보조 메서드
    def _siftdown(self, idx): # 내부적으로 사용할 메서드
        # 초기화
        smallest = idx # 가장 작은 요소 = 0
        left = idx * 2 + 1 # 왼쪽 자식 = 0 * 2 + 1 = 1
        right = idx * 2 + 2 # 오른쪽 자식 = 0 * 2 + 2 = 2

        if left < self.length and self.heap[left] < self.heap[smallest]: # 왼쪽 자식이 더 작은 값인 경우
            smallest = left
        if right < self.length and self.heap[right] < self.heap[smallest]: # 오른쪽 자식이 더 작은 값인 경우
            smallest = right
        if smallest != idx: # 더 작은 값이 존재하는 경우
            self.heap[smallest], self.heap[idx] = self.heap[idx], self.heap[smallest] # 스왑
            self._siftdown(smallest) # 힙 속성이 유지될 때까지

    def __str__(self):
        return str(self.heap)  # 힙의 문자열 표현 반환

# 최소 힙: 루트 노드가 최소
min_heap = MinHeap()
min_heap.heappush(3)
min_heap.heappush(1)
min_heap.heappush(2)

print(min_heap)  # [1, 3, 2]
print(min_heap.heappop())  # 1
print(min_heap)  # [2, 3]

min_heap.heapify([5, 4, 3, 2, 1])
print(min_heap)  # [1, 2, 3, 5, 4]
print(min_heap.heappop())  # 1
print(min_heap)  # [2, 4, 3, 5] 
print(min_heap.heappop())  # 2
print(min_heap)  # [3, 4, 5]