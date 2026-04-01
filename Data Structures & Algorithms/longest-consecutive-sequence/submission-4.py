class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        numSet = set(nums)
        for num in nums:
            left = num - 1
            if left not in numSet:
                streak = 1
                curr = num
                while (curr + 1) in numSet:
                    streak = streak + 1
                    curr = curr + 1
                if streak > longest:
                    longest = streak
        return longest