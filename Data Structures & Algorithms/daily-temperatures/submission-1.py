class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #0, 
        stack = []
        res = len(temperatures) * [0]
        for i in range (0, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[len(stack) - 1]]:
                res[stack[len(stack) - 1]] = i - stack[len(stack) - 1]
                stack.pop()
            stack.append(i)
        return res