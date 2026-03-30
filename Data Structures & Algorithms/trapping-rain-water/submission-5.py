class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxR = 0
        maxL = 0

        amount = 0
        while l < r:
            amount = amount + max(0, min(maxL, maxR) - height[l])
            amount = amount + max(0, min(maxL, maxR) - height[r])

            if height[l] > maxL:
                maxL = height[l]
            
            if height[r] > maxR:
                maxR = height[r]

            if height[l] > height[r]:
                r = r - 1
            else:
                l = l + 1
        return amount