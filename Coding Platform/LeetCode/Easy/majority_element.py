from typing import List
import numpy as np
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n1 = np.array(nums)
        Count = np.array(np.unique(n1,return_counts=True))
        i = np.where(Count[1] == max(Count[1]))
        return int(Count[0][i])
