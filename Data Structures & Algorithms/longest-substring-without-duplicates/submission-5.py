class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(len(s))
        l = 0
        r = 1

        res = 1
        if not s:
            return 0
        seenLets = set()
        seenLets.add(s[l])
        while l <= r and r < len(s) and l < len(s):
            if s[r] not in seenLets:
                winSize = r - l + 1
                if winSize > res:
                    res = winSize
                seenLets.add(s[r])
                r = r + 1
            else:
                seenLets.remove(s[l])
                l = l + 1
        return res