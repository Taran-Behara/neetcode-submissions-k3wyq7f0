class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sHash = {}
        for c in s:
            if c in sHash:
                sHash[c] = sHash[c] + 1
            else:
                sHash[c] = 1
        

        tHash = {}
        for c in t:
            if c in tHash:
                tHash[c] = tHash[c] + 1
            else:
                tHash[c] = 1
        

        for key in sHash:
            if key not in tHash or tHash[key] != sHash[key]:
                return False
            
        return True