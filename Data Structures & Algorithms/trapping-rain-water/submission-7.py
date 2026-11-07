class Solution:
    def trap(self, height: List[int]) -> int:
        #min(maxL, maxR) - curr

        maxL = []
        maxR = [0] * len(height)

        currMax = 0
        for i in range(0, len(height)):
            maxL.append(currMax)
            currMax = max(height[i], currMax)
        
        i = len(height) - 1
        currMax = 0

        while i >= 0:
            maxR[i] = currMax
            currMax = max(height[i], currMax)
            i -= 1

        res = 0
        for i in range(0, len(height)):
            res += max(0, min(maxL[i], maxR[i]) - height[i])
        
        return res