from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        Data = {"2": ["a", "b", "c"],"3": ["d", "e", "f"],"4": ["g", "h", "i"],
        "5": ["j", "k", "l"],"6": ["m", "n", "o"],"7": ["p", "q", "r", "s"], 
        "8": ["t", "u", "v"],"9": ["w", "x", "y","z"]  }
        Temp = []
        for i in digits:
            if(i in Data):
                Temp.append(Data[i])
        Data.clear()
        Data = list(Data)
        if(len(Temp) == 4):
            for i in Temp[0]:
                for j in Temp[1]:
                    for k in Temp[2]:
                        for l in Temp[3]:
                            Data.append(i+j+k+l)
            del(Temp)
            return Data
        if(len(Temp) == 3):
            for i in Temp[0]:
                for j in Temp[1]:
                    for k in Temp[2]:
                        Data.append(i+j+k)
            del(Temp)
            return Data
        if(len(Temp) == 2):
            for i in Temp[0]:
                for j in Temp[1]:
                    Data.append(i+j)
            del(Temp)
            return Data
        elif(len(Temp) == 1):
            return Temp[0]
        else:
            return []

            