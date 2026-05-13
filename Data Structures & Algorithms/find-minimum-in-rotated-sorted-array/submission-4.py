class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        res = float("inf")

        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < res:
                    res = nums[l]
                break
            check = (l + r) // 2
            if nums[check] < res:
                res = nums[check]

            if nums[check] >= nums[l]:
                l = check + 1
            else:
                r = check - 1
        
        return res