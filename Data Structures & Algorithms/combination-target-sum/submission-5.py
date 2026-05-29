class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(curr, index, target):
            if index >= len(nums) or target < 0:
                return
            
            if target == 0:
                toAdd = curr.copy()
                res.append(toAdd)
                return
            
            curr.append(nums[index])
            dfs(curr, index, target - nums[index])
            while (index + 1) < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            curr.pop()
            dfs(curr, index + 1, target)
        
        dfs([], 0, target)
        return res