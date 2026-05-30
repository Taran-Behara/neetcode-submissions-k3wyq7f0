class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(curr):
            if not curr:
                return [[]]
            res = []
            for i in range(0, len(curr)):
                rest = dfs(curr[0:i] + curr[i + 1:])
                for arr in rest:
                    arr.append(curr[i])
                    res.append(arr)
            
            return res
        
        return dfs(nums)