from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        L = len(mat) // 2
        j = 0
        Sum = 0
        for i in range(len(mat)):
            Sum += mat[i][j] + mat[i][-(j+1)]
            j += 1
        if(len(mat) % 2 != 0):
            Sum -= mat[L][L]
        return Sum