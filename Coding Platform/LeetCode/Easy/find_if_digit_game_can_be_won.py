from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum = [0,0]
        for i in nums:
            if(i < 10):
                sum[0] += i
            else:
                sum[1] += i
        if(sum[0] > sum[1] or sum[1] > sum[0]):
            return True
        else:
            return False