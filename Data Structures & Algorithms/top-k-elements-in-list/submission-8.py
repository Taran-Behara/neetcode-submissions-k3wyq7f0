class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = []
        for num in nums:
            freqs.append([])

        freqMap = {}
        for num in nums:
            if num in freqMap:
                freqMap[num] = freqMap[num] + 1
            else:
                freqMap[num] = 1
        
        
        for key in freqMap:
            numFrequency = freqMap[key]
            freqs[numFrequency - 1].append(key)

        
        i = len(freqs) - 1
        freqMax = []
        print(freqMap)
        print(freqs)
        while i >= 0 and len(freqMax) < k:
            if freqs[i] != []:
                j = 0
                while j < len(freqs[i]) and len(freqMax) < k:
                    freqMax.append(freqs[i][j])
                    j = j + 1
            i = i - 1
        return freqMax