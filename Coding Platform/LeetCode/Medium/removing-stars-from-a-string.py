class Solution:
    def removeStars(self, s: str) -> str:
        Stack = []
        for i in s:
            if(i == "*"):
                Stack.pop(-1)
            else:
                Stack.append(i)
        return "".join(Stack)