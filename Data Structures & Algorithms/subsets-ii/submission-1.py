class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def dfs(curr, index):
            if index >= len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[index])
            dfs(curr, index + 1)
            curr.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            dfs(curr, index + 1)
        
        dfs([], 0)
        return res