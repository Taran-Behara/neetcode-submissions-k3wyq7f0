class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for num in stones:
            heap.append(num * -1)
        heapq.heapify(heap)
        while len(heap) >= 2:
            one = -heapq.heappop(heap)
            two = -heapq.heappop(heap)

            if one != two:
                heapq.heappush(heap, -(one - two))
        
        if heap:
            return heap[0] * -1
        
        return 0