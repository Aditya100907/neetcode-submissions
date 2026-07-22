class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        best = 0
        for price in prices:
            if price < low:
                low = price
            else:
                best = max(best, price - low)
        return best
            
