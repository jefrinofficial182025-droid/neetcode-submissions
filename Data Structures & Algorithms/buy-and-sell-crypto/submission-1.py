class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,maxprofit = 0,0
        min_so_far = prices[0]
        for price in prices: 
            min_so_far = min(min_so_far,price)
            profit = price - min_so_far
            maxprofit = max(maxprofit,profit)
        return maxprofit

        