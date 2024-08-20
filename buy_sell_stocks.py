class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day_of_min_price = prices.index(min(prices))
        day_of_max_price = prices.index(max(prices[day_of_min_price:]))
        return prices[day_of_max_price] - prices[day_of_min_price]
        
