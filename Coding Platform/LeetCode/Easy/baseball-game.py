from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        Temp = []
        for i in range(len(operations)):
            if(operations[i] == "+"):
                Temp.append(Temp[-1]+Temp[-2])
            elif(operations[i] == "D"):
                Temp.append(Temp[-1] * 2)
            elif(operations[i] == "C"):
                Temp.pop()
            else:
                Temp.append(int(operations[i]))
        return sum(Temp)