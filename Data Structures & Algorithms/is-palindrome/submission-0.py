class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for letter in s:
            if letter.isalnum():
                word += letter

        word = word.lower()
        left = 0
        right = len(word) - 1
        while left < right:
            if word[left] is not word[right]:
                return False
            left += 1
            right -= 1
        return True