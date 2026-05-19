class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        res = 0
        for num in nums:
            if num - 1 not in numSet:
                currStreak = 1
                currNum = num + 1
                while currNum in numSet:
                    currNum += 1
                    currStreak += 1
                
                res = max(res, currStreak)
        
        return res