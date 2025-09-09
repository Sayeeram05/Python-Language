from typing import List


class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        i = 0
        for j in arr:
            if(i < 2) or (arr[i-2] != j):
                arr[i] = j
                i += 1
        return i  