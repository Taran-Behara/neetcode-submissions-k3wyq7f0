class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            check = (l + r) // 2

            if nums[check] == target:
                return check
            elif nums[check] > target:
                r = check - 1
            else:
                l = check + 1
        
        return -1