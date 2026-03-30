class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)

        res = 0
        for num in nums:
            left = num - 1
            if left not in setNums:
                streak = 1
                right = num + 1
                while right in setNums:
                    streak = streak + 1
                    right = right + 1
                res = max(res, streak)
        return res