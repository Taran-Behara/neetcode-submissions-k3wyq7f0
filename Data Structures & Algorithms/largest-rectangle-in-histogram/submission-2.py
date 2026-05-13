class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(0, len(heights)):
            if not stack:
                toAdd = []
                toAdd.append(i)
                toAdd.append(heights[i])
                stack.append(toAdd)
            else:
                startIndex = i
                while stack and heights[i] < stack[len(stack) - 1][1]:
                    top = stack[len(stack) - 1]
                    area = (i - top[0]) * top[1]
                    
                    maxArea = max(maxArea, area)
                    startIndex = top[0]
                    stack.pop()
                toAdd = []
                toAdd.append(startIndex)
                toAdd.append(heights[i])
                stack.append(toAdd)
        
        while stack:
            top = stack[len(stack) - 1]
            area = (len(heights) - top[0]) * top[1]
            maxArea = max(area, maxArea)
            stack.pop()
        
        return maxArea