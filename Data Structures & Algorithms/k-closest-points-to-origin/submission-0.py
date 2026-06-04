class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calcDistance(point):
            xSq = point[0] ** 2
            ySq = point[1] ** 2

            return math.sqrt(xSq + ySq)
        
        pointToDist = {}
        for point in points:
            pointToDist[tuple(point)] = calcDistance(point)
        
        heap = []
        for point in pointToDist:
            heapq.heappush(heap, (pointToDist[point], point))
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        
        return res
