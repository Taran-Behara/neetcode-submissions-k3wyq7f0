class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # def dfs(curr):
        #     if not curr:
        #         return [[]]
        #     res = []
        #     for i in range(0, len(curr)):
        #         rest = dfs(curr[0:i] + curr[i + 1:])
        #         for arr in rest:
        #             arr.append(curr[i])
        #             res.append(arr)
            
        #     return res
        res = []
        def dfs(start, curr):
            if start == len(curr):
                res.append(curr[:])
                return
            for i in range(start, len(curr)):
                curr[i], curr[start] = curr[start], curr[i]
                dfs(start + 1, curr)
                curr[i], curr[start] = curr[start], curr[i]
        dfs(0, nums)
        return res