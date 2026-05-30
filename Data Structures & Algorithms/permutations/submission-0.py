class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, rem):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(0, len(rem)):
                toAdd = curr.copy()
                toAdd.append(rem[i])
                first = rem[0:i]
                second = rem[i + 1:len(rem)] if i + 1 < len(rem) else []
                newRem = first + second
                dfs(toAdd, newRem)
        dfs([], nums)
        return res
            
