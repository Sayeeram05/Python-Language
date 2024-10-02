class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = list(str(int(a) + int(b)))
        if('2' not in ans):
            return "".join(ans)
        ans.reverse()
        for i in range(len(ans)):
            try:
                if(ans[i] == '2'):
                    ans[i] = '0'
                    ans[i+1] = str(int(ans[i+1])+1)
                elif(ans[i] == '3'):
                    ans[i] = '1'
                    ans[i+1] = str(int(ans[i+1])+1)
            except:
                ans.append('1')
        ans.reverse()
        return "".join(ans)