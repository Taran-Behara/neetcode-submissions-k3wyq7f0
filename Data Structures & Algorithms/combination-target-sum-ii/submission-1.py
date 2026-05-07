class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def dfs(currSum, currArray, currIndex):
            if currSum == target:
                res.append(currArray)
                return
            
            if currSum > target or currIndex >= len(candidates):
                return

            nArray = currArray.copy()
            nArray.append(candidates[currIndex])
            dfs(currSum + candidates[currIndex], nArray, currIndex + 1)

            while currIndex + 1 < len(candidates) and candidates[currIndex] == candidates[currIndex + 1]:
                currIndex += 1
            
            dfs(currSum, currArray, currIndex + 1)
        
        dfs(0, [], 0)
        return res