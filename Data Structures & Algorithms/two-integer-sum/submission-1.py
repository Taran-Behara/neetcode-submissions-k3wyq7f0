class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        res = []
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in h:
                res.append(h[complement])
                res.append(i)
                return res
            h[nums[i]] = i
        return res