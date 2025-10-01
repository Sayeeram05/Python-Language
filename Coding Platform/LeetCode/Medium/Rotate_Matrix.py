class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        Temp = []
        for i in matrix:
            Temp.append(i.copy())
        for i in range(len(Temp)):
            L = len(Temp[i]) - 1 - i
            for j in range(len(Temp[i])):
                matrix[j][L] = Temp[i][j]