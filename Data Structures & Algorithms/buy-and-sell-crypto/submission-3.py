class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0
        while r < len(prices) and l < r:
            if prices[r] < prices[l]:
                l = r
                r = r + 1
            else:
                profit = prices[r] - prices[l]
                if profit > res:
                    res = profit
                r = r + 1
        return res