class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        else:
            Sums = sum(nums)
            L = len(nums)
            i = 0
            arraylen = L -1
            while(arraylen != 0):
                if(arraylen == 1):
                    Max = max(nums)
                    if(Max > Sums):
                        return Max
                    arraylen -= 1
                elif(i+arraylen <= L):
                    Sum = sum(nums[i:i+arraylen])
                    if(Sum > Sums):
                        Sums = Sum
                    i += 1  
                else:
                    i = 0
                    arraylen -= 1
            return Sums

            
