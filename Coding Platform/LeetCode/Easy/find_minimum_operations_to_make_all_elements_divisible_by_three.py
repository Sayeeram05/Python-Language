from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = 0
        for i in nums:
            if(i % 3 != 0):
                if(((i+1)%3) == 0 or ((i-1)%3) == 0):
                    n += 1
        return n