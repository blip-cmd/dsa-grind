class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
         #thought
        #  iterate through and swap at certain points: i tried drawing and figuring a relation...i saw the column was constant and the row counted but i couldn't map that to a loop till i saw the transpose reverse suggestion in the discussions.
        # to do a 90degree rotation, u'd transpose and then reverse the rows
        n = len(matrix)
        for i in range(n):
            # print(i)
            for j in range(i+1, n):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
        

        #reverse row
        for row in matrix:
            row.reverse()