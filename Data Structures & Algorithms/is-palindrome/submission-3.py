class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""

        for char in s:
            if char.isalnum():
                t = t + char.lower()
        l = 0
        r = len(t) - 1
        while l <= r:
            if t[r] != t[l]:
                return False
            l = l + 1
            r = r - 1
        
        return True