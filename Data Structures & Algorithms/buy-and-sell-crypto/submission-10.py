class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0

        maxProfit = 0

        while l <= r and r < len(prices):
            profit = prices[r] - prices[l]

            maxProfit = max(maxProfit, profit)

            if prices[l] > prices[r]:
                l = l + 1
            else:
                r = r + 1
        
        return maxProfit