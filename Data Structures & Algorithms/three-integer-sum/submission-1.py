class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(0, len(nums)):
            comp = 0 - nums[i]
            twoSum = set()
            for j in range(i + 1, len(nums)):
                jComp = comp - nums[j]
                if jComp in twoSum:
                    toAdd = []
                    toAdd.append(nums[i])
                    toAdd.append(jComp)
                    toAdd.append(nums[j])
                    toAdd.sort()
                    if toAdd not in res:
                        res.append(toAdd)
                else:
                    twoSum.add(nums[j])
            #twoSum.clear()
        return res
