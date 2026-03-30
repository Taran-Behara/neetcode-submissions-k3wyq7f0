class Solution:
    def isPalindrome(self, s: str) -> bool:
        alstr = ""
        for char in s:
            if char.isalnum():
                alstr = alstr + char
        
        left = 0
        right = len(alstr) - 1
        alstr = alstr.lower()
        
        while left <= right:
            if alstr[left] != alstr[right]:
                return False
            left = left + 1
            right = right - 1
        return True