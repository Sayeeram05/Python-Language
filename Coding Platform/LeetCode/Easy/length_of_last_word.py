class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = -1
        l = 0
        while(abs(i) <= len(s)):
            if(s[i]==" " and l>0):
                return l
            elif(s[i].isalpha()):
                l += 1
            i -= 1
        return l