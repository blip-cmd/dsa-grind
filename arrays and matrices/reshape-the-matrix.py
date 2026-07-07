class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        rows, cols = len(mat), len(mat[0])

        if rows*cols != r*c:
            return mat

        flat_mat = []
        for row in mat:
            for x in row:
                flat_mat.append(x)
        
        result = [[0 for _ in range(c)] for _ in range(r) ]

        k = 0 
        for i in range(r):
            for j in range(c):
                result[i][j] = flat_mat[k]
                k += 1
        
        return result