class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = str(x)
        if( i == i[-1::-1]):
            return(True)