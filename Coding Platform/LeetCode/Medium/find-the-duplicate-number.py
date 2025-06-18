from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        L = len(nums)
        for i in range(0,L-1):
            if(nums[i] == nums[i+1]):
                return nums[i]