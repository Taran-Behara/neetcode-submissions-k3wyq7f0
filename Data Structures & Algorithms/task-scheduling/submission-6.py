class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {}
        for task in tasks:
            if task in freqs:
                freqs[task] += 1
            else:
                freqs[task] = 1
        
        heap = []
        for key in freqs:
            heapq.heappush(heap, [-freqs[key], key])
        

        q = collections.deque()
        res = []
        tasksComp = 0
        time = 0
        while tasksComp < len(tasks):
            if heap:
                top = heapq.heappop(heap)
                res.append(top[1])
                top[0] = top[0] + 1
                timeAvailable = time + n
                if top[0] != 0:
                    q.appendleft((timeAvailable, top))
                tasksComp += 1
            else:
                res.append("i")
            if q:
                qTop = q[len(q) - 1]
                if qTop[0] <= time:
                    qTop = q.pop()
                    heapq.heappush(heap, qTop[1])
            time += 1
        #     print(heap)
        #     print(q)
        #     print(res)
        #     print()
        # print(res)
        return len(res)


