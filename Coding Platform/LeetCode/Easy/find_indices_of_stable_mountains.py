from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        stable = []
        for i in range(1,len(height)):
            if(height[i - 1] > threshold):
                stable.append(i)
        return(stable)