class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        result = 0
        while l < r and l < len(prices) and r < len(prices):
            if prices[r] <= prices[l]:
                l = r
                r = l + 1
            else:
                tot = prices[r] - prices[l]
                if tot > result:
                    result = tot
                r = r + 1
        return result