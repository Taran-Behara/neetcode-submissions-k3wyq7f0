class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapOne = {}

        for c in s1:
            if c in mapOne:
                mapOne[c] = mapOne[c] + 1
            else:
                mapOne[c] = 1
        

        l = 0
        r = 0
        mapTwo = {}

        while l <= r and r < len(s2):
            if s2[r] in mapTwo:
                mapTwo[s2[r]] = mapTwo[s2[r]] + 1
            else:
                mapTwo[s2[r]] = 1


            windowSize = r - l + 1
            if windowSize < len(s1):
                r = r + 1
                continue
            
            match = True

            print(s2[l:r + 1])
            print(mapTwo)
            print()

            for key in mapOne:
                if key not in mapTwo or mapTwo[key] != mapOne[key]:
                    match = False
            
            if match:
                return True
            
            if mapTwo[s2[l]] <= 1:
                mapTwo.pop(s2[l])
            else:
                mapTwo[s2[l]] = mapTwo[s2[l]] - 1
            l = l + 1
            r = r + 1
        
        return False
             