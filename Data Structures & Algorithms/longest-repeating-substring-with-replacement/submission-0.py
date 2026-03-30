class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        result = 0
        charCount = {}
        addedInd = set()
        while l <= r and l < len(s) and r < len(s):
            if s[r] in charCount and r not in addedInd:
                charCount[s[r]] = charCount[s[r]] + 1
                addedInd.add(r)
            elif r not in addedInd:
                charCount[s[r]] = 1
                addedInd.add(r)
            
            maxVal = 0
            for i in charCount:
                if charCount[i] > maxVal:
                    maxVal = charCount[i]
            winSize = r - l + 1
            numR = winSize - maxVal
            if numR <= k:
                r = r + 1
                if winSize > result:
                    result = winSize
            else:
                charCount[s[l]] = charCount[s[l]] - 1
                l = l + 1
        return result