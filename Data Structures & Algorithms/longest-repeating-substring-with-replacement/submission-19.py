class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        r = 0
        maxCount = 0
        count = {}
        rChange = True
        while l <= r and r < len(s):
            if s[r] in count and rChange:
                count[s[r]] = count[s[r]] + 1
            elif rChange:
                count[s[r]] = 1

            maxCount = max(maxCount, count[s[r]])
            print(s[l:(r + 1)])
            print(maxCount)
            print(count)
            reps = (r - l + 1) - maxCount
            print(reps)
            print()
            if reps <= k:
                length = r - l + 1
                if length > longest:
                    longest = length
                rChange = True
                r = r + 1
            else:
                rChange = False
                count[s[l]] = count[s[l]] - 1
                l = l + 1
            
        return longest