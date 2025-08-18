from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        Output = []
        Max = max(candies)
        for i in range(len(candies)):
            if((candies[i] + extraCandies) < Max):
                Output.append(False)
            else:
                Output.append(True)
        return Output
