class Solution:
    def longestPalindrome(self, s: str) -> str:
        def Check(Left,Right):
            while(Left >= 0 and Right < len(s) and s[Left] == s[Right]):
                Left -= 1
                Right += 1
            return s[Left+1:Right]
        Longest = ""
        for i in range(len(s)):
            Center1 = Check(i,i)
            Center2 = Check(i,i+1)

            if(Center1 == Center1[::-1] and len(Center1) > len(Longest)):
                Longest = Center1
            if(Center2 == Center2[::-1] and len(Center2) > len(Longest)):
                Longest = Center2
        return Longest


        


        
