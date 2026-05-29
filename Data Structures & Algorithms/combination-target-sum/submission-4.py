class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        seen = set()
        def dfs(curr, index, target):
            if index >= len(nums) or target < 0:
                return
            
            if target == 0:
                toAdd = curr.copy()
                res.append(toAdd)
                return
            
            toAdd = curr.copy()
            toAdd.append(nums[index])

            dfs(toAdd, index, target - nums[index])
            while (index + 1) < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            dfs(curr, index + 1, target)
        
        dfs([], 0, target)
        return res