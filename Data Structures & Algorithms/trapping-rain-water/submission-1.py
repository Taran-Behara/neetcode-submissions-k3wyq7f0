class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        lMax = height[l]
        rMax = height[r]

        res = 0
        while l < r:
            if lMax < rMax:
                l = l + 1
                lMax = max(height[l], lMax)
                res = res + lMax - height[l]
            else:
                r = r - 1
                rMax = max(height[r], rMax)
                res = res + rMax - height[r]
        return res