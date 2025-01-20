class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if(x < 0):
            sign = -1
        x = abs(x)
        val = 0
        while(x>0):
            val = (val*10) + (x % 10)
            x = x // 10
        print(val)
        if(-2**31 < val and val < 2**31-1):
            if(sign == -1):
                return -val
            return val
        return 0