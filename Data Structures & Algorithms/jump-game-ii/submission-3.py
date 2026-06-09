class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dfs(index):
            if index == len(nums) - 1:
                return 0
            
            if index in memo:
                return memo[index]
            a = float("infinity")
            for i in range(1, nums[index] + 1):
                if index + i < len(nums):
                    b = dfs(index + i)
                    a = min(a, b)
            memo[index] = a + 1
            return a + 1
        return dfs(0)