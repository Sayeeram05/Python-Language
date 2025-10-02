class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        Zeros = []
        for i in range(len(matrix)):
            if(0 in matrix[i]):
                for j in range(len(matrix[i])):
                    if(matrix[i][j] == 0):
                        Zeros.append([i,j])
        for i in Zeros:
            for j in range(len(matrix[i[0]])):
                matrix[i[0]][j] = 0
            for j in range(len(matrix)):
                matrix[j][i[1]] = 0