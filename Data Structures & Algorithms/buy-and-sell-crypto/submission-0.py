class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        p = 0
        for i in range(len(prices)):
            p = max(prices[i] - minbuy, p)
            minbuy = min(minbuy, prices[i])
        
        return p
