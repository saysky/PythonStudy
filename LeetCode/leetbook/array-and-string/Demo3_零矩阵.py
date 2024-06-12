import copy


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        # [1,0,2,1],
        # [3,4,5,2],
        # [1,3,1,5]
        # 只要出现0，将该行该列设为0
        # rowIndex=0, columnIndex=1
        def setRowZero(matrix, rowIndex):
            for j in range(len(matrix[rowIndex])):
                matrix[rowIndex][j] = 0

        def setColumnZero(matrix, columnIndex):
            for i in range(len(matrix)):
                matrix[i][columnIndex] = 0

        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = copy.deepcopy(matrix)
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                if temp[i][j] == 0:
                    setRowZero(matrix, i)
                    setColumnZero(matrix, j)
