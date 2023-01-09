class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        low = prices[0]
        high = prices[0]
        for i in range(len(prices)):
            if prices[i] > high:
                high = prices[i]
                if high - low > r:
                    r = high - low
            elif prices[i] < low:
                low = prices[i]
                high = prices[i]
            
        return r