class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0
        for price in prices:
            profit = price - buy
            maxProfit = max(maxProfit, profit)
            buy = min(buy, price)
        return maxProfit
