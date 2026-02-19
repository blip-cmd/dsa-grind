class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # row = mid // n 
        # col = mid % n

        n = len(matrix[0])
        l,r = 0, n-1
        while l<=r:
            mid = (l+r)//2

            row = mid // n 
            col = mid % n

            if matrix[row][col] == target:
                return True #bool(mid)
            elif matrix[row][col] < target:
                l = mid+1
            else:
                r = mid-1
        
        return False #bool(0)
        