class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        numToStr = {}
        numToStr[2] = ["a", "b", "c"]
        numToStr[3] = ["d", "e", "f"]
        numToStr[4] = ["g", "h", "i"]
        numToStr[5] = ["j", "k", "l"]
        numToStr[6] = ["m", "n", "o"]
        numToStr[7] = ["p", "q", "r", "s"]
        numToStr[8] = ["t", "u", "v"]
        numToStr[9] = ["w", "x", "y", "z"]
    
        res = []
        def helper(currStr: str, currDig: int):
            if (currDig >= len(digits)):
                res.append(currStr)
                return currStr
        
            strArray = numToStr[int(digits[currDig])]
            for char in strArray:
                exStr = currStr
                exStr = exStr + char
                helper(exStr, currDig + 1)
        helper("", 0)
        return res