class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        self.preSum = [[0] * (COLS+1) for r in range(ROWS+1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.preSum[r][c+1]
                self.preSum[r+1][c+1] = prefix + above

    def sumRegion(self, r1, c1, r2, c2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        bottomRight = self.preSum[r2+1][c2+1]
        above = self.preSum[r1][c2+1]
        left = self.preSum[r2+1][c1]
        topLeft = self.preSum[r1][c1]
    
        return bottomRight - left - above + topLeft




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)