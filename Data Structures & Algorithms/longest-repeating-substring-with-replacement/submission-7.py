class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0

        letCount = {}
        res = 0
        while l <= r and r < len(s):
            if r == 0 and s[r] in letCount:
                letCount[s[r]] = letCount[s[r]] + 1
            elif r == 0:
                letCount[s[r]] = 1
            
            
            maxRep = 0
            for key in letCount:
                if letCount[key] > maxRep:
                    maxRep = letCount[key]
            
            winSize = r - l + 1
            if winSize - maxRep <= k:
                if winSize > res:
                    res = winSize
                r = r + 1
                if r < len(s) and s[r] in letCount:
                    letCount[s[r]] = letCount[s[r]] + 1
                elif r < len(s):
                    letCount[s[r]] = 1
            else:
                if s[l] in letCount:
                    letCount[s[l]] = letCount[s[l]] - 1
                    if letCount [s[l]] <= 0:
                        del letCount[s[l]]
                l = l + 1
        return res