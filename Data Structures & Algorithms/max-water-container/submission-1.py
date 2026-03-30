class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            amount = (r - l) * min(heights[l], heights[r])
            if amount > maxAmount:
                maxAmount = amount
            
            if heights[l] <= heights[r]:
                l = l + 1
            else:
                r = r - 1
        return maxAmount