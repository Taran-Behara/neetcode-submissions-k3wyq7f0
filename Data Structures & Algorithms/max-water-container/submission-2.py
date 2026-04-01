class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxArea = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            if area > maxArea:
                maxArea = area
            
            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        
        return maxArea