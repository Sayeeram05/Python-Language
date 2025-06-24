class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        for i in t:
            if(i not in s or t.count(i) != s.count(i)):
                return(i)
           