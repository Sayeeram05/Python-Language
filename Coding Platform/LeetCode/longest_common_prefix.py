class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        L = len(min(strs, key=len))
        for i in range(L):
            for j in range(1,len(strs)):
                if(strs[0][i] == strs[j][i]):
                    continue
                else:
                    return common
            common += strs[0][i]  
        return common