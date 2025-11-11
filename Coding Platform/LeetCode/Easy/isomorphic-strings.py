class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        DataS = dict()
        DataT = dict()
        for i in range(len(s)):
            if(s[i] in DataS):
                DataS[s[i]][0] += 1
                DataS[s[i]][1].append(i)
            else:
                DataS[s[i]] = [1,[i]]
            if(t[i] in DataT):
                DataT[t[i]][0] += 1
                DataT[t[i]][1].append(i)
            else:
                DataT[t[i]] = [1,[i]]
        if(len(DataS) != len(DataT)):
            return False

        for i in DataS:
            for j in DataT:
                if(DataS[i] == DataT[j]):
                    DataT.pop(j)
                    break
            else:
                return False
        return True