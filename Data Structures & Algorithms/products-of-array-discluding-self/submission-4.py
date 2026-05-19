class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        lp = 1
        rp = 1

        for num in nums:
            res.append(lp)
            lp *= num
        
        ind = len(nums) - 1
        while ind >= 0:
            res[ind] *= rp
            rp *= nums[ind]
            ind -= 1
        
        return res