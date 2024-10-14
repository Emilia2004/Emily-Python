class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max = 0
        buy =  prices[0]
        prices = prices[1:]
        for sell in prices:
            if sell-buy<0:
                buy = sell
            if sell-buy>max:
                max = sell-buy
        return max