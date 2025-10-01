from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        L = len(nums)
        while k > L:
            k -= L
        if(k == 1):
            Temp = nums[-1:] + nums[:-1]
            nums[:] = Temp[:]
        elif(k > 0):
            Temp = nums[L-k:] + nums[:L-k]
            nums[:] = Temp[:]

        