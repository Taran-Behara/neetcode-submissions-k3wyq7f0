class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = 0
        maxR = 0

        l = 0
        r = len(height) - 1
        amount = 0

        while l < r:
            amount = amount + max(0, min(maxL, maxR) - height[l])
            amount = amount + max(0, min(maxL, maxR) - height[r])

            if height[r] > maxR:
                maxR = height[r]
            
            if height[l] > maxL:
                maxL = height[l]
            
            if height[l] > height[r]:
                r = r - 1
            else:
                l = l + 1
        return amount