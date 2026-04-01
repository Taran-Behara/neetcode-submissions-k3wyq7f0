class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = [0] * len(nums)

        lp = 1
        rp = 1

        for num in nums:
            left.append(lp)
            lp = lp * num
        
        index = len(nums) - 1
        while index >= 0:
            right[index] = rp
            rp = rp * nums[index]
            index = index - 1

        res = []
        for i in range(0, len(nums)):
            res.append(left[i] * right[i])
        return res