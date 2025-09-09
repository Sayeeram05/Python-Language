class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s.reverse()
        while(" " in s):
            s.remove(" ")
        s = " ".join(s)
        return(s)