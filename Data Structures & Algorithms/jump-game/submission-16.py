class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        dp[len(nums) - 1] = True
        i = len(nums) - 2
        while i >= 0:
            place = False
            for j in range(i, i + nums[i] + 1):
                if j in dp and dp[j]:
                    place = True
            
            dp[i] = place
            i -= 1
        
        return dp[0]
        