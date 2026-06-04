class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.heap.append(num * -1)
        heapq.heapify(self.heap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val * -1)

        count = 0
        num = -1
        removed = []
        while count < self.k:
            num = heapq.heappop(self.heap)
            removed.append(num)
            count += 1
        
        for num in removed:
            heapq.heappush(self.heap, num)
        
        return num * -1