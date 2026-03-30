class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        r = 1
        result = 1
        seen = set()
        while l < r and l < len(s) and r < len(s):
            if not seen:
                seen.add(s[l])
            if s[r] in seen:
                l = l + 1
                r = l + 1
                seen.clear()
            else:
                length = r - l + 1
                if length > result:
                    result = length
                seen.add(s[r])
                r = r + 1
        return result