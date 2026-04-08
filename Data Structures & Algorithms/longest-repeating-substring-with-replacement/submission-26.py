class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0

        l = 0
        r = 0

        rChange = True
        while l <= r and r < len(s):
            if rChange:
                if s[r] in count:
                    count[s[r]] += 1
                else:
                    count[s[r]] = 1
            maxCount = 0
            for key in count:
                maxCount = max(maxCount, count[key])
            
            windowSize = r - l + 1

            reps = windowSize - maxCount

            if reps <= k:
                rChange = True
                longest = max(longest, windowSize)
                r = r + 1
            else:
                rChange = False
                if count[s[l]] >= 1:
                    count[s[l]] -= 1
                l = l + 1
        return longest