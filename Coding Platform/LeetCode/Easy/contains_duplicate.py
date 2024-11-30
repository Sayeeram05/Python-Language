from typing import List
import numpy as np

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        df = np.array(nums)
        return (len(np.unique(df)) != len(df))