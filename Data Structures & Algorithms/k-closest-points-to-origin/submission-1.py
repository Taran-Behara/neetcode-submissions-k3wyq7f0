class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calcDistance(point):
            xSq = point[0] ** 2
            ySq = point[1] ** 2

            return math.sqrt(xSq + ySq)
        
        heap = []
        for point in points:
            heapq.heappush(heap, (-calcDistance(point), point))
            if len(heap) > k:
                heapq.heappop(heap)

        
        res = []
        for point in heap:
            res.append(point[1])
        return res
