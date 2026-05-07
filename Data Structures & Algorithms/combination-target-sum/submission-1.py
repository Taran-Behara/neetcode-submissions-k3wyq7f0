class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(currSum, currArray, currIndex):
            if currSum == target:
                if currArray not in res:
                    res.append(currArray)
                return
            elif currSum > target:
                return

            if currIndex >= len(nums):
                return
            
            dfs(currSum, currArray, currIndex + 1)
            nArray = currArray.copy()
            nArray.append(nums[currIndex])
            dfs(currSum + nums[currIndex], nArray, currIndex + 1)
            dfs(currSum + nums[currIndex], nArray, currIndex)
        dfs(0, [], 0)
        return res
