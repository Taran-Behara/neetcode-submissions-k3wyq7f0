class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            numOne = nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                numTwo = nums[l]
                numThree = nums[r]
                threeSum = numOne + numTwo + numThree

                if threeSum > 0:
                    r = r - 1
                elif threeSum < 0:
                    l = l + 1
                else:
                    toAdd = []
                    toAdd.append(numOne)
                    toAdd.append(numTwo)
                    toAdd.append(numThree)
                    res.append(toAdd)

                    l = l + 1
                    while l < r and nums[l] == nums[l - 1]:
                        l = l + 1
        return res


