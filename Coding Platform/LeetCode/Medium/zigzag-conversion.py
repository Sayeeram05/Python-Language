class Solution:
    def convert(self, s: str, numRows: int) -> str:
        Data = [[] for _ in range(numRows)]
        j = 0
        check = False
        for i in s:
            if(j == numRows):
                check = False
                j -= 2
            if(j <= 0):
                j = 0
                check = True
            if(j < numRows and check):
                Data[j].append(i)
                j += 1
            else:
                Data[j].append(i)
                j -= 1
        print(Data)
        S = ""
        for i in Data:
            S += "".join(i)
        return S


            