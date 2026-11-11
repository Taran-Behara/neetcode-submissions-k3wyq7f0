class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i in range(0, len(heights)):
            if not stack or heights[i] > stack[-1][1]:
                stack.append((i, heights[i]))
            else:
                startIndex = i
                while stack and heights[i] <= stack[-1][1]:
                    area = (i - stack[-1][0]) * stack[-1][1]
                    res = max(res, area)
                    startIndex = stack[-1][0]
                    stack.pop()
                
                stack.append((startIndex, heights[i]))
        
        while stack:
            area = (len(heights) - stack[-1][0]) * stack[-1][1]
            res = max(res, area)
            stack.pop()
        
        return res