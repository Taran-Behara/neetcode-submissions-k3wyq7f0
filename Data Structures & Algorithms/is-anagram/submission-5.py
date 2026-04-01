class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        sMap = {}
        tMap = {}

        for char in s:
            if char in sMap:
                sMap[char] = sMap[char] + 1
            else:
                sMap[char] = 1
        
        for char in t:
            if char in tMap:
                tMap[char] = tMap[char] + 1
            else:
                tMap[char] = 1
        
        for char in s:
            if char in tMap:
                if tMap[char] != sMap[char]:
                    return False
            else:
                return False
        
        return True