class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        lets = {}
        lets["2"] = "abc"
        lets["3"] = "def"
        lets["4"] = "ghi"
        lets["5"] = "jkl"
        lets["6"] = "mno"
        lets["7"] = "pqrs"
        lets["8"] = "tuv"
        lets["9"] = "wxyz"

        res = []
        def dfs(curr, index):
            if index >= len(digits):
                res.append(curr)
                return
            
            poss = lets[digits[index]]
            for char in poss:
                temp = curr
                curr += char
                dfs(curr, index + 1)
                curr = temp
        
        dfs("", 0)
        return res