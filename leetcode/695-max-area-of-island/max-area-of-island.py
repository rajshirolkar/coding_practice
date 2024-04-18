class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(r,c):
            if r<0 or c<0 or r>= ROWS or c>=COLS or not grid[r][c]:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1)

        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i,j))
        return maxArea