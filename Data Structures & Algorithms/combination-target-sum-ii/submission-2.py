class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        print(candidates)
        def dfs(index, curr, target):
            if target == 0:
                res.append(curr.copy())
                return

            if index >= len(candidates) or target < 0:
                return
            
            
            curr.append(candidates[index])
            dfs(index + 1, curr, target - candidates[index])
            curr.pop()
            i = index
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, target)
        
        dfs(0, [], target)
        return res