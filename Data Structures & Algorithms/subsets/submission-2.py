class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = [[]]
        def dfs(curr, nums, index):
            if index >= len(nums):
                return
            
            toAdd = curr.copy()
            self.res.append(toAdd)
            toAdd.append(nums[index])
            dfs(curr, nums, index + 1)
            dfs(toAdd, nums, index + 1)
        
        dfs([], nums, 0)
        return self.res
