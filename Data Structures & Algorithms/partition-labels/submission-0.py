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
        curr = ""
        for i in range(0, len(s)):
            if i > earliest:
                res.append(curr)
                curr = ""
            
            curr += s[i]
            
            earliest = max(earliest, lastIndex[s[i]])
        res.append(curr)
        for i in range(0, len(res)):
            res[i] = len(res[i])
        return res