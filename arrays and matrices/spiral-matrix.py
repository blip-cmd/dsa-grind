# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         #the pattern i see
#         result contains first row in array
        #it then contains the  last element of the second row -> or simply elements of the last column then it goes to the bottom row ....naa i realize this pattern would change a lot for growing rows...i checked the contraints for that ,it's 10. new approach needed.

        # thinking...
#         matrix = [  [1,2,3,4],
#                     [5,6,7,8],
#                     [9,10,11,12]
#                     [13,14,15,16]
#                 ]

#     [00 01 02 03
#      10 11 12 13
#      20 21 22 23 
#      30 31 32 33]


# Output: [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

#idea 2
# it seems as though we are iterating through the grid in left-right direction, top to bottom direction, bottom to top and then right to left. direction changes when we hit the boundary. boundary can be wall or that the next telement is already in the result group.
#trying to model the direction changes:
# - start left to right.
#     move down on col bound.
#         move left on row bound
#             move up on col bound
#                 more right when next up-item is in result
#                     move down when next right-item is in result     
#                         OR end if next right-item is in result AND next down-item is in result
#                     move left..repeat.till all next items in result then end.
#reviewing the approach,
# result group checks would be growing inefficiently 

# #updated approach:
# - shrink the edges
# - a check is needed to avoide double work

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
            
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while left <= right and top <= bottom:
            # 1, Move Right across the top row
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            
            # 2, Move Down the right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            # The Guard Check for unexpected matrix shapes
            if not (left <= right and top <= bottom):
                break
             
            # 3, Move Left across the bottom row
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
                pass
            bottom -= 1
            
            # 4, Move Up the left column
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
                pass
            left += 1
            
        return res
