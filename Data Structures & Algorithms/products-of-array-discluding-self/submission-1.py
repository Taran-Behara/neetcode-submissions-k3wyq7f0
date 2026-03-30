class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #1, 1, 2, 8
        #1, 6, 24, 48
        #48, 24, 6, 1

        left = []
        product = 1
        for num in nums:
            left.append(product)
            product = product * num
        
        right = [0] * len(nums)
        product = 1
        index = len(nums) - 1
        while index >= 0:
            right[index] = product
            product = product * nums[index]
            index = index - 1

        res = []
        for index in range(0, len(nums)):
            product = left[index] * right[index]
            res.append(product)
        return res
        

