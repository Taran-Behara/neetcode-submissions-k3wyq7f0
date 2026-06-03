class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(s):
            l = 0
            r = len(s) - 1

            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        

        res = []

        def dfs(curr, index):
            if index >= len(s):
                res.append(curr.copy())
                return
            
            for i in range(index, len(s)):
                part = s[index:i + 1]
                if isPal(part):
                    curr.append(part)
                    dfs(curr, i + 1)
                    curr.pop()
        
        dfs([], 0)
        return res