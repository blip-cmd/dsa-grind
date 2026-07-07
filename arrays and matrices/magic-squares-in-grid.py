class Solution:
      # we need a way to check a 3x3 sub matrix from a cell point. 
            # - i'd say the +1,-1 to r and c and r-1,c+1 and r-1,c-1 and r+1,c-1,r+1,c+1
            #so two loops and the above is the second. 
                # in it, you'd use a list:1..9 to confirm if valid, when 1 invalid, return False for that sub_matrix. if all valide, increment counter of magic matrixes.
                #in first loop, also ensure each number is <16.
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        def is_magic(r, c):
            # grab the 3x3 block using the center point r,c
            # use +/- 1 to get all neighbors
            around = [
                grid[r-1][c-1], grid[r-1][c], grid[r-1][c+1], # top
                grid[r][c-1],   grid[r][c],   grid[r][c+1],   # mid
                grid[r+1][c-1], grid[r+1][c], grid[r+1][c+1]  # bot
            ]
            
            # make sure it's exactly 1-9 distinct
            if sorted(around) != list(range(1, 10)):
                return False
            
            # check the 8 sums (must be 15)
            # rows
            if sum(around[0:3]) != 15: return False
            if sum(around[3:6]) != 15: return False
            if sum(around[6:9]) != 15: return False
            
            # cols
            if around[0] + around[3] + around[6] != 15: return False
            if around[1] + around[4] + around[7] != 15: return False
            if around[2] + around[5] + around[8] != 15: return False
            
            # diags
            if around[0] + around[4] + around[8] != 15: return False
            if around[2] + around[4] + around[6] != 15: return False
            
            return True

        # start at 1 and end at -1 to stay inside the 3x3 boundary
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if is_magic(i, j):
                    count += 1
                    
        return count