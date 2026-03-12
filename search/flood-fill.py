class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        start_color =  image[sr][sc]
        rows,cols = len(image) , len(image[0]) 

        def dfs(r, c):
            if image[r][c] == start_color:
                image[r][c] = color
                for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                    if 0 <= nr < rows and 0 <= nc < cols:
                        dfs(nr, nc)

        dfs(sr,sc)               
        return image
