class MedianFinder:
    # 3, 5, 2, 7, 1, 6, 4
    # 1234567

    # Min = [3, 4, 5, 6, 7], Max = [2, 1]
    # Min = [4, 5, 6, 7], Max = [3, 2, 1]
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.minHeap or num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        
        while abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                top = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -top)
            else:
                top = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -top)


    def findMedian(self) -> float:
        print(self.minHeap)
        print(self.maxHeap)
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            #print((self.minHeap[0] + (-self.maxHeap[0])) / 2)
            print()
            return (self.minHeap[0] + (-self.maxHeap[0])) / 2
        
        print()
        if self.maxHeap and len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return self.minHeap[0] 