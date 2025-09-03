class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = j = 0
        while i < len(nums):
            if(i > j):
                return False
            else:
                j = max(j,i+nums[i])
                i += 1
        return True
                     
