class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            check = (l + r)//2
            if nums[check] == target:
                return check
            if nums[check] >= nums[l]:
                if target > nums[check] or target < nums[l]:
                    l = check + 1
                else:
                    r = check - 1
            else:
                if target < nums[check] or target > nums[r]:
                    r = check - 1
                else:
                    l = check + 1

        return -1