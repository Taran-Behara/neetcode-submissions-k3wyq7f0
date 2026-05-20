class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = 0
        r = sum(weights)

        res = r
        while l <= r:
            mid = (l + r) // 2
            currWeight = 0
            currDays = 1

            ind = 0
            while ind < len(weights):
                if mid < weights[ind]:
                    currDays = -1
                    break
                elif currWeight + weights[ind] > mid:
                    currWeight = 0
                    currDays += 1

                currWeight += weights[ind]
                ind += 1
            
            if currDays != -1 and currDays <= days:
                r = mid - 1
                res = min(res, mid)
            else:
                l = mid + 1
        
        return res