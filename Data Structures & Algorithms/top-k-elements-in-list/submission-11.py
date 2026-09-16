class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = {}
        for num in nums:
            if num in numToFreq:
                numToFreq[num] += 1
            else:
                numToFreq[num] = 1
        
        freqToNum = []
        for i in range(0, len(nums) + 1): freqToNum.append([])

        for num in numToFreq:
            freqToNum[numToFreq[num]].append(num)
        
        res = []
        
        arrInd = len(freqToNum) - 1
        while arrInd >= 0:
            arr = freqToNum[arrInd]
            if arr:
                i = len(arr) - 1
                while i >= 0 and len(res) < k:
                    res.append(arr[i])
                    i -= 1
            arrInd -= 1
        
        return res