class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}

        for char in t:
            if char in tCount:
                tCount[char] += 1
            else:
                tCount[char] = 1
        
        l = 0
        sCount = {}
        need = len(tCount)
        have = 0
        res = ""
        for r in range(0, len(s)):
            char = s[r]
            if char in sCount:
                sCount[char] += 1
            else:
                sCount[char] = 1

            if char in tCount and tCount[char] == sCount[char]:
                have += 1
            

            print(s[l:r+1])
            print(have)
            print(need)
            print()
            if have == need:
                while l <= r and have == need:
                    length = r - l + 1
                    if res == "" or length < len(res):
                        res = s[l:r+1]
                    char = s[l]
                    if char in tCount and tCount[char] == sCount[char]:
                        have -= 1
                    if sCount[char] > 1:
                        sCount[char] -= 1
                    else:
                        sCount.pop(char)
                    l += 1
        
        return res

