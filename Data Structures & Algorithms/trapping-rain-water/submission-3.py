class Solution:
    def trap(self, height: List[int]) -> int:
        #0,2,0,3,1,0,1,3,2,1

        #min(maxL, maxR) - h[i]

        amount = 0

        maxLH = 0
        maxL = []
        for num in height:
            maxL.append(maxLH)
            if num > maxLH:
                maxLH = num
        
        maxRH = 0
        maxR = [0] * len(height)
        index = len(height) - 1
        while index >= 0:
            maxR[index] = maxRH
            if height[index] > maxRH:
                maxRH = height[index]
            index = index - 1
        
        print(maxL)
        print(maxR)

        for i in range(0, len(height)):
            amount = amount + max(0, min(maxL[i], maxR[i]) - height[i])
        return amount