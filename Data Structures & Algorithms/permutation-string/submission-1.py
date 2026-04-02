class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapOne = {}
        rChange = True

        for c in s1:
            if c in mapOne:
                mapOne[c] = mapOne[c] + 1
            else:
                mapOne[c] = 1


        l = 0
        r = 0
        
        mapTwo = {}
        while l <= r and r < len(s2):
            if rChange:
                if s2[r] in mapTwo:
                    mapTwo[s2[r]] = mapTwo[s2[r]] + 1
                else:
                    mapTwo[s2[r]] = 1

            windowSize = r - l + 1
            if windowSize < len(s1):
                rChange = True
                r = r + 1
                continue
            rChange = False

            print(s2[l: r + 1])
            print(mapTwo)
            print()

            match = True
            for key in mapTwo:
                if key not in mapOne or mapOne[key] != mapTwo[key]:
                    match = False

            if match:
                return True

            if mapTwo[s2[l]] > 1:
                mapTwo[s2[l]] = mapTwo[s2[l]] - 1
            else:
                mapTwo.pop(s2[l])

            l = l + 1

        return False            