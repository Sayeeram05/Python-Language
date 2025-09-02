from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        self.nums1 = nums1 

        self.nums1 = self.nums1[:m]
        self.nums1.extend(nums2[:n])
        self.nums1.sort()
        nums1[:] = self.nums1