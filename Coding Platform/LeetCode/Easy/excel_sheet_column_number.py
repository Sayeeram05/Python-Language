from string import ascii_uppercase as UP
class Solution(object):
    def titleToNumber(self, columnTitle):
        L = len(columnTitle)
        value = 0
        if(L > 1):
            for i in columnTitle[:-1]:
                L -= 1
                value += (26 ** L) * (UP.index(i) + 1)
                print(value)
            value += (UP.index(columnTitle[-1]) + 1)
        else:
            value = UP.index(columnTitle) + 1
        return value