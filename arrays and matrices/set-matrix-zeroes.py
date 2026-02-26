# class Solution(object):
#     def setZeroes(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """

#         # #inital idea
#         # iterate through the matrix
#         # if item is a 0, store the col and row number in a list
#         # else:
#         # crosscheck the list and make current element 0


#         # #space O(m+n)
#         # rows, cols = len(matrix), len(matrix[0])
#         # zero_rows, zero_cols = set(), set()

#         # # First, store the row and col of zeros
#         # for r in range(rows):
#         #     for c in range(cols):
#         #         if matrix[r][c] == 0:
#         #             zero_rows.add(r)
#         #             zero_cols.add(c)

#         # # After, set the zeros
#         # for r in range(rows):
#         #     for c in range(cols):
#         #         if r in zero_rows or c in zero_cols:
#         #             matrix[r][c] = 0
        
#         # return None


#space O(1)
def setZeroes(matrix):
    matrix = matrix #pass by reference, so we can modify the original matrix
    rows, cols = len(matrix), len(matrix[0])
    
    # Flags to remember if first row/col should be zeroed
    first_row_zero = 0 in matrix[0]
    first_col_zero = 0 in (matrix[r][0] for r in range(rows))
    # print("first_row_zero:", first_row_zero )
    # print("first_col_zero:", first_col_zero)
    
    # Use first row and column as markers
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0
    
    # Apply markers to inner matrix
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
    
    # Handle first row
    if first_row_zero:
        for c in range(cols):
            matrix[0][c] = 0
    
    # Handle first column
    if first_col_zero:
        for r in range(rows):
            matrix[r][0] = 0
            
    return matrix #returning for testing purposes, but the problem states to modify in-place and return None

assert setZeroes([[1,1,1],[1,0,1],[1,1,1]]) == [[1,0,1],[0,0,0],[1,0,1]]
assert setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]) == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
assert setZeroes([[1,0,3]]) == [[0,0,0]]
assert setZeroes([[1],[0],[3]]) == [[0],[0],[0]]

