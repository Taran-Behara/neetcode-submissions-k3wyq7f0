class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)


        res = 0
        for num in nums:
            check = num - 1
            if check not in numSet:
                currStreak = 0
                curr = num
                while curr in numSet:
                    currStreak += 1
                    curr += 1
                
                res = max(res, currStreak)
        
        return res