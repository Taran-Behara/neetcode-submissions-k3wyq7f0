class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = {}
        for num in nums:
            if num in numToFreq:
                numToFreq[num] += 1
            else:
                numToFreq[num] = 1
        
        freqToNum = []
        for i in range(0, len(nums) + 1):
            freqToNum.append([])
        for key in numToFreq:
            freqToNum[numToFreq[key]].append(key)
        

        freqInd = len(freqToNum) - 1
        res = []
        while freqInd >= 0 and len(res) < k:
            arrInd = len(freqToNum[freqInd]) - 1
            while arrInd >= 0 and len(res) < k:
                res.append(freqToNum[freqInd][arrInd])
                arrInd -= 1
            freqInd -= 1
        
        return res