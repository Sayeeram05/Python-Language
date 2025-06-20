from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = current = 0
        for i in nums:
            if(i == 1):
                current += 1
            elif(current > max):
                max = current
                current = 0
            else:
                current = 0
        if(current > max):
            return current
        return max