class Solution:
    def isPalindrome(self, s: str) -> bool:
        curr = ""
        for c in s:
            if c.isalnum():
                curr += c.lower()
        

        l = 0
        r = len(curr) - 1
        

        while l <= r:
            if curr[l] != curr[r]:
                return False
            l += 1
            r -= 1
        
        return True