class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        res = []

        for i in range(0, len(nums)):
            complement = target - nums[i]

            if complement in numMap:
                res.append(numMap[complement])
                res.append(i)
            else:
                numMap[nums[i]] = i
        
        return res