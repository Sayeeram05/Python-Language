class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Length = 0
        visited = []
        for i in s:
            if(i in visited):
                L = len(visited)
                if(L > Length):
                    Length = L
                visited = visited[visited.index(i)+1:]
                visited.append(i)
                continue
            else:
                visited.append(i)
        L = len(visited)
        if(L > Length):
            Length = L
        return(Length)