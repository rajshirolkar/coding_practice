class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(row, col):
            if row<0 or col<0 or row >= ROWS or col >= COLS or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        
        res = 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    dfs(i,j)
                    res += 1
        return res