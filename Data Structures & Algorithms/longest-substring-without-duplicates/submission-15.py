class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()

        l = 0
        for r in range(0, len(s)):
            if s[r] not in seen:
                length = r - l + 1
                longest = max(length, longest)
                seen.add(s[r])
            else:
                print(s[l:r])
                print(seen)
                while l < r and s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
                print(s[l:r])
                print(seen)
                print()
        
        return longest