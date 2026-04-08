class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1C = {}
        for char in s1:
            if char in s1C:
                s1C[char] += 1
            else:
                s1C[char] = 1
        
        s2C = {}
        l = 0
        r = 0

        rChange = True
        while l <= r and r < len(s2):
            if rChange:
                char = s2[r]
                if char in s2C:
                    s2C[char] += 1
                else:
                    s2C[char] = 1
            
            windowSize = r - l + 1
            if windowSize < len(s1):
                rChange = True
                r = r + 1
                continue

            print(s2[l:r+1])
            print(s2C)
            print()
            
            match = True
            for key in s2C:
                if key not in s1C or s2C[key] != s1C[key]:
                    match = False
            
            if match:
                return True
            
            if s2C[s2[l]] > 1:
                s2C[s2[l]] -= 1
            else:
                s2C.pop(s2[l])
            l = l + 1
            rChange = False
        
        return False
