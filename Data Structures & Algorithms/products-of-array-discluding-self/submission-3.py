class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        lp = 1
        rp = 1

        for num in nums:
            res.append(lp)
            lp = lp * num
        
        index = len(nums) - 1
        while index >= 0:
            res[index] = rp * res[index]
            rp = rp * nums[index]
            index = index - 1
        return res