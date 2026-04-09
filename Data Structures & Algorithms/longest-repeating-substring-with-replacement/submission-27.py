class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        count = {}

        l = 0
        for r in range(0, len(s)):
            char = s[r]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
            
            maxCount = 0
            for key in count:
                maxCount = max(maxCount, count[key])
            
            while l < r and r - l + 1 - maxCount > k:
                if count[s[l]] > 1:
                    count[s[l]] -= 1
                else:
                    count.pop(s[l])
                l += 1
            longest = max(longest, r - l + 1)
        return longest