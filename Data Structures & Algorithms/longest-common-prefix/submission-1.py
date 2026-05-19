class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        def findPrefix(s1, s2):
            l = 0
            r = 0
            ind = 0
            while l < len(s1) and r < len(s2):
                if s1[l] == s2[r]:
                    ind += 1
                    l += 1
                    r += 1
                else:
                    break
                
            return s1[0:ind]
        
        if len(strs) == 1:
            return strs[0]
        
        res = findPrefix(strs[0], strs[1])
        for s in strs:
            res = findPrefix(res, s)
        
        return res