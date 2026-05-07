class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        numToLet = {}
        numToLet["2"] = "abc"
        numToLet["3"] = "def"
        numToLet["4"] = "ghi"
        numToLet["5"] = "jkl"
        numToLet["6"] = "mno"
        numToLet["7"] = "pqrs"
        numToLet["8"] = "tuv"
        numToLet["9"] = "wxyz"

        res = []

        def dfs(digIndex, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                currStr = ""
                return currStr
            
            currLets = numToLet[digits[digIndex]]
            for let in currLets:
                dfs(digIndex + 1, currStr + let)
        
        dfs(0, "")
        
        return res
            

