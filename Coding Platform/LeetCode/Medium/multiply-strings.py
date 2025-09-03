class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        Data = {str(i):i for i in range(10)}
        X = 0
        for i in num1:
            X = X*10 + Data[i]
        Y = 0
        for i in num2:
            Y = Y*10 + Data[i]
        X *= Y
        print(X)
        Data = {i:str(i) for i in range(10)}
        num1 = ""
        while(X != 0):
            Y = X % 10
            num1 += Data[Y]
            X //= 10
        if(num1 == ""):
            return "0"
        return num1[-1::-1]