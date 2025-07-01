from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        CurrentSum = MaxSum = nums[0]
    
        for value in nums[1:]:
            CurrentSum = max(value,CurrentSum+value)
            MaxSum = max(CurrentSum,MaxSum)
            
        return MaxSum

            
