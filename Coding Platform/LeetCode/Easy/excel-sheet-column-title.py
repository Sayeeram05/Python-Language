class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        output = ""
        while columnNumber > 0:
            columnNumber -= 1
            output += chr(65 + columnNumber % 26)
            columnNumber //= 26
        return(output[::-1])
