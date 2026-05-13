class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)

        res = r
        while l <= r:
            check = (l + r)//2
            if check == 0:
                break

            hoursReq = 0
            for num in piles:
                hoursReq += math.ceil(num/check)
            
            if hoursReq <= h:
                res = check
                r = check - 1
            else:
                l = check + 1
        
        return res