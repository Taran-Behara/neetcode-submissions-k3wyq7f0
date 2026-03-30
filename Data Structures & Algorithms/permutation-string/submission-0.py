class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}
        for s in s1:
            if s in s1Count:
                s1Count[s] = s1Count[s] + 1
            else:
                s1Count[s] = 1
        
        l = 0
        r = 0

        s2Count = {}
        while l <= r and l < len(s2) and r < len(s2):
            if s2[r] in s2Count:
                s2Count[s2[r]] = s2Count[s2[r]] + 1
            else:
                s2Count[s2[r]] = 1
            
            winSize = r - l + 1
            if winSize == len(s1):
                if s2Count == s1Count:
                    return True
                else:
                    s2Count.clear()
                    l = l + 1
                    r = l
            else:
                r = r + 1
        return False