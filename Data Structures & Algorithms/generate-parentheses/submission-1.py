class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr, closed, numOpen):
            if numOpen == n and numOpen == closed:
                res.append(curr)
                return
            
            if numOpen == n:
                dfs(curr + ')', closed + 1, numOpen)
                return
            
            if numOpen == closed:
                dfs(curr + '(', closed, numOpen + 1)
                return
            
            dfs(curr + '(', closed, numOpen + 1)
            dfs(curr + ')', closed + 1, numOpen)

        dfs("", 0, 0)
        return res