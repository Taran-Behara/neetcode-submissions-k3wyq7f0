class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #10, 1, 5, 6, 7, 1
        l = 0
        r = 1

        profit = 0
        while l <= r and r < len(prices):
            if prices[l] > prices[r]:
                l = l + 1
            else:
                currP = prices[r] - prices[l]
                if currP > profit:
                    profit = currP
                r = r + 1
        return profit
