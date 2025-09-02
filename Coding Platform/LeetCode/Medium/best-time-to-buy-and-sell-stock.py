from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Profit = 0
        X = None
        Y = None
        for i in prices:
            if(X == None or Y == None):
                X = i
                Y = i
            elif(i < X):
                X = i
                Y = i
            else:
                Y = i
            if((Y-X) > Profit):
                Profit = Y-X
        return Profit
            
                