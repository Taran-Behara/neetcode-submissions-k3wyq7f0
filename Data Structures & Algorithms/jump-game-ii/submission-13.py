class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = 0
        r = 0

        while r < len(nums) - 1:
            max_in_range = 0
            for i in range(l, r + 1):
                max_in_range = max(nums[i], max_in_range)
            
            l = r + 1
            r += max_in_range
            jumps += 1
        
        return jumps

            
