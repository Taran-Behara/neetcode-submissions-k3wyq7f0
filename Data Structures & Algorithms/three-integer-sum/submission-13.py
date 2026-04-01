class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                currSum = nums[i] + nums[l] + nums[r]

                if currSum > 0:
                    r = r - 1
                    while nums[r] == nums[r + 1]:
                        r = r - 1
                elif currSum < 0:
                    l = l + 1
                    while nums[l] == nums[l - 1]:
                        l = l + 1
                else:
                    toAdd = []
                    toAdd.append(nums[i])
                    toAdd.append(nums[l])
                    toAdd.append(nums[r])
                    res.append(toAdd)
                    r = r - 1
                    while r > 0 and nums[r] == nums[r + 1]:
                        r = r - 1
                    l = l + 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l = l + 1
        return res