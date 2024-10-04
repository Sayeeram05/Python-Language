from math import factorial as FA
class Solution:
    def climbStairs(self, n: int) -> int:
        Two = n // 2
        Ways = 0
        
        for r in range(1,Two+1):
            N = (n - (r * 2)) + r
            if(N == 0):
                return n
            # print("N",N,"n",n,"r",r)
            Ways += (FA(N) // (FA(r)*(FA(N-r))))

        return Ways+1