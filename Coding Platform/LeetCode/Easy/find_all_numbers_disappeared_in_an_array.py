from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        L = set(range(1,len(nums)+1))
        nums = set(nums)
        return(list(L-nums))
        