class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        sMap = {}
        for c in t:
            if c in tMap:
                tMap[c] = tMap[c] + 1
            else:
                tMap[c] = 1
                sMap[c] = 0
        
        have = 0
        need = len(tMap)

        l = 0
        r = 0
        res = ""
        addedInd = set()
        while l <= r and l < len(s) and r < len(s):
            if s[r] in sMap and r not in addedInd:
                sMap[s[r]] = sMap[s[r]] + 1
                addedInd.add(r)
                if sMap[s[r]] == tMap[s[r]]:
                    have = have + 1
            
            if have == need:
                if res == "" or (r - l + 1) < len(res):
                    res = s[l:(r + 1)]
                if s[l] in sMap:
                    sMap[s[l]] = sMap[s[l]] - 1
                    if sMap[s[l]] < tMap[s[l]]:
                        have = have - 1
                l = l + 1
            else:
                r = r + 1
        return res