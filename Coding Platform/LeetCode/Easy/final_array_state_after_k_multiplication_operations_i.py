from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            m = nums.index(min(nums))
            nums[m] *= multiplier
        return(nums)