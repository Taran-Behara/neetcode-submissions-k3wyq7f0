class MedianFinder:
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
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            #print((self.minHeap[0] + (-self.maxHeap[0])) / 2)
            print()
            return (self.minHeap[0] + (-self.maxHeap[0])) / 2
        
        if self.maxHeap and len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return self.minHeap[0] 