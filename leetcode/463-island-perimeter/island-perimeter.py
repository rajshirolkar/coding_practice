class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r,c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or not grid[r][c]:
                return 1
            
            if (r,c) in visit:
                return 0
            
            visit.add((r,c))

            peri = dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1)
            return peri

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    return dfs(i,j)