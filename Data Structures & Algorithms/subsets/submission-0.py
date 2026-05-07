class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(currArray, numIndex):
            if numIndex == len(nums):
                res.append(currArray)
                return currArray

            dfs(currArray, numIndex + 1)
            nArray = currArray.copy()
            nArray.append(nums[numIndex])
            dfs(nArray, numIndex + 1)
        
        dfs([], 0)
        return res