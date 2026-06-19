class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        i = len(s) - 1
        while i >= 0:
            if s[i] not in lastIndex:
                lastIndex[s[i]] = i
            
            i -= 1
        
        earliest = 0
        res = []
        l = 0
        r = 0
        for i in range(0, len(s)):
            if i > earliest:
                res.append(r - l)
                l = r
            r += 1
            
            earliest = max(earliest, lastIndex[s[i]])

        res.append(r - l)
        return res