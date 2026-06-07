class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = {}
        for task in tasks:
            if task in freqMap:
                freqMap[task] += 1
            else:
                freqMap[task] = 1
        
        heap = []

        for key in freqMap:
            heapq.heappush(heap, [-freqMap[key], key])
        
        res = []
        tasksProcessed = 0
        while heap:
            top = heap[0][1]
            idle = False

            if res:
                newHeap = []
                while top in res[max(0,len(res) - n):len(res)]:
                    if not heap:
                        res.append("i")
                        idle = True
                        break
                    oldTop = heapq.heappop(heap)
                    heapq.heappush(newHeap, oldTop)
                    if heap:
                        top = heap[0][1]
                if not idle:
                    tasksProcessed += 1
                    res.append(top)
                    toAdd = heapq.heappop(heap)
                    toAdd[0] = toAdd[0] + 1
                    if toAdd[0] < 0:
                        heapq.heappush(newHeap, toAdd)
                while newHeap:
                    t = heapq.heappop(newHeap)
                    heapq.heappush(heap, t)
            else:
                tasksProcessed += 1
                res.append(top)
                toAdd = heapq.heappop(heap)
                toAdd[0] = toAdd[0] + 1
                if toAdd[0] < 0:
                    heapq.heappush(heap, toAdd)
            
            #print(heap)
        #     print(res)
        #     print()
        # print(res)
        return len(res)

