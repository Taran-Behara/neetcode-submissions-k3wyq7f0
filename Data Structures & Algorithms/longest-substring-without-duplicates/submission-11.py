class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #abcabcbb
        
        longest = 0
        l = 0
        r = 0
        seen = set()
        while l <= r and r < len(s):
            if s[r] not in seen:
                length = r - l + 1
                if length > longest:
                    longest = length
                seen.add(s[r])
                r = r + 1
            else:
                seen.remove(s[l])
                l = l + 1
        return longest