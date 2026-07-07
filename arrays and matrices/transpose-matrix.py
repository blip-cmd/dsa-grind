class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        nROWS = len(matrix)
        nCOLS = len(matrix[0])

        result = [[0]*nROWS for _ in range(nCOLS)]

        for i in range(nROWS):
            for j in range(nCOLS):
                result[j][i] = matrix[i][j] 
        
        return result
        