class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = []
        left = []

        lp = 1
        for n in nums:
            left.append(lp)
            lp *= n
        
        
        index = len(nums) - 1
        rp = 1
        while index >= 0:
            right.append(rp)
            rp *= nums[index]
            index -= 1
        
        res = []
        for i in range(0, len(nums)):
            res.append(left[i] * right[len(right) - i - 1])
        
        return res