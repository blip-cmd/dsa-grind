import __main__
from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        n, m = len(grid), len(grid[0])
        visited = set()

        def bfs(i, j):
            queue = deque([(i, j)])
            visited.add((i, j))
            while queue:
                r, c = queue.popleft()
                for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                    if (0 <= nr < n and 0 <= nc < m 
                        and (nr, nc) not in visited and grid[nr][nc] == "1"):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1

        return islands

if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    print("Grid:")
    for row in grid:
        print(" ".join(row))

    solution = Solution()
    result = solution.numIslands(grid)
    print(f"Number of islands: {result}")