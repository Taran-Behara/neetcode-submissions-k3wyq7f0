class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = {}

        for num in nums:
            if num in numToFreq:
                numToFreq[num] = numToFreq[num] + 1
            else:
                numToFreq[num] = 1
        

        freqToNum = []

        for num in nums:
            freqToNum.append([])

        for key in numToFreq:
            freq = numToFreq[key]
            freqToNum[freq - 1].append(key)


        res = []
        index = len(freqToNum) - 1
        #[1], [2, 3]

        while index >= 0 and len(res) < k:
            currArray = freqToNum[index]
            j = 0
            while j < len(currArray) and len(res) < k:
                res.append(currArray[j])
                j = j + 1
            index = index - 1
        return res
