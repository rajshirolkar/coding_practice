class Solution:
    def findFarmland(self, grid: List[List[int]]) -> List[List[int]]:
        # DFS approach
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j]==0:
                return (-1,-1)
            grid[i][j] = 0
            i1,j1 = dfs(i+1, j)
            i2,j2 = dfs(i-1, j)
            i3,j3 = dfs(i, j+1)
            i4,j4 = dfs(i, j-1)
            return (max(i,i1,i2,i3,i4), max(j,j1,j2,j3,j4))
        res = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    min_x, min_y = row, col
                    max_x, max_y = dfs(row, col)
                    res.append([min_x,min_y, max_x, max_y])
        return res