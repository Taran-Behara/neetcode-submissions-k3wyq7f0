class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        l = 0
        r = 0

        currMax = float("-inf")
        while l <= r and r < len(nums):
            currMax = max(currMax, nums[r])

            length = r - l + 1
            if length == k:
                l += 1
                res.append(currMax)
                currMax = float("-inf")
                r = l
            else:
                r = r + 1
        
        return res
