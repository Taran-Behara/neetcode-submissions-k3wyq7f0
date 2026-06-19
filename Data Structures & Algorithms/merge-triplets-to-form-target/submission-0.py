class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = []
        for t in triplets:
            isGood = True
            for i in range(0, 3):
                if t[i] > target[i]:
                    isGood = False
            
            if isGood:
                good.append(t)
        
        print(good)
        
        for i in range(0, 3):
            num = target[i]
            isGood = False
            for t in good:
                if t[i] == num:
                    isGood = True
            
            if not isGood:
                return False
            
        return True