class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-1
        while(i > 0):
            if(nums[i-1] < nums[i]):
                i -= 1
                break
            i -=  1
        if(max(nums) == nums[i]):
            nums.sort()
        else:
            Temp = nums[i+1:]
            Temp.sort()
            j = 0
            for k in Temp:
                if(k > nums[i]):
                    j = k
                    break
            for k in range(len(nums)-1,i,-1):
                if(nums[k] == j):
                    j = k
                    break
            
            nums[i],nums[j] = nums[j],nums[i]

            Temp = nums[i+1:]
            Temp.sort()          
            nums[i+1:] = Temp
        