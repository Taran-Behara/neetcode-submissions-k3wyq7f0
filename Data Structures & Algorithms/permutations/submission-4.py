class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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