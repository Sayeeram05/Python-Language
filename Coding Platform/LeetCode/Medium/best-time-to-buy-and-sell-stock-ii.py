from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Buy = Profit = 0
        for i in range(1,len(prices)):
            if(prices[i-1] < prices[i]):
                Profit += prices[i] - prices[i-1]
        return Profit
