class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            guess = (l + r)//2
            if nums[guess] == target:
                return guess
            elif nums[guess] > target:
                r = guess - 1
            else:
                l = guess + 1
        
        return -1