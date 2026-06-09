class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        dp[len(nums) - 1] = 0
        index = len(nums) - 2
        while index >= 0:
            a = float("inf")
            for i in range(1, nums[index] + 1):
                if index + i in dp:
                    a = min(a, dp[index + i])
            
            dp[index] = a + 1
            index -= 1
        print(dp)
        return dp[0]