class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0

        seen = set()
        maxLength = 0
        while l <= r and r < len(s):
            if s[r] not in seen:
                length = r - l + 1
                maxLength = max(maxLength, length)
                seen.add(s[r])
                r = r + 1
            else:
                seen.remove(s[l])
                l = l + 1
        
        return maxLength
