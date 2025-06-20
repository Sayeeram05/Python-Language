from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Dict = {}
        Max = [0,0]
        for i in nums:
            if(i in Dict):
                Dict[i] += 1
            else:
                Dict[i] = 1
            if(Dict[i] > Max[1]):
                Max[0],Max[1] = i,Dict[i]
        return Max[0]
        