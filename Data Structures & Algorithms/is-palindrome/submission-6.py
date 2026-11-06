class Solution:
    def isPalindrome(self, s: str) -> bool:
        curr = ""
        for c in s:
            if c.isalnum():
                curr += c.lower()
        

        l = 0
        r = len(curr) - 1
        print(curr)
        while l < r and curr[l] == curr[r]:
            l += 1
            r -= 1
        print(l)
        print(r)
        return l == r or (l == (r + 1))