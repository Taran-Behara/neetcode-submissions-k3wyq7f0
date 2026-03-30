class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = {}
        tmap = {}

        for char in s:
            if char in smap:
                smap[char] = smap[char] + 1
            else:
                smap[char] = 1
        
        for char in t:
            if char in tmap:
                tmap[char] = tmap[char] + 1
            else:
                tmap[char] = 1


        for char in s:
            if char not in tmap:
                return False
            elif smap[char] != tmap[char]:
                return False
        
        return True
