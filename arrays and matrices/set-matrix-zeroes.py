class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # #inital idea
        # iterate through the matrix
        # if item is a 0, store the col and row number in a list
        # else:
        #      crosscheck the list and make current element 0

        #code
        
        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        # First, store the row and col of zeros
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        # After, set the zeros
        for r in range(rows):
            for c in range(cols):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0
        
        return None
