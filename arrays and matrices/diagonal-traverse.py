class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        result = []

        m,n = len(mat) , len(mat[0])
        

        #on diagonals: d
        for d in range(m+n-1):
            #even: go up
            if d%2==0:
                r = min(d, m-1) #bottom
                c = d - r # c+r = d 
                while r>=0 and c <= n -1:
                    result.append(mat[r][c])
                    r -= 1
                    c += 1 
            else:
                #odd: go down
                c = min(d,n-1)
                r = d - c
                while c >=0 and r <= m-1:
                    result.append(mat[r][c])
                    r += 1
                    c -= 1

        return result