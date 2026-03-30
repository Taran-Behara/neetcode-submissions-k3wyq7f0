class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] = freqs[num] + 1
            else:
                freqs[num] = 1
        
        pq = []
        
        for key in freqs:
            heapq.heappush(pq, (freqs[key] * -1, key))
        
        print(pq)
        count = k
        res = []
        while k > 0:
            c = heapq.heappop(pq)
            res.append(c[1])
            k = k - 1
        return res

        
