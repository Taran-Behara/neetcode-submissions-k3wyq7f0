class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0

        for r in range(0, len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
                r = r + 1
            else:
                while l < r and prices[l] >= prices[r]:
                    l = l + 1
        
        return maxProfit