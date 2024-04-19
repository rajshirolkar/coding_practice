class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS approach
        ROWS, COLS = len(grid), len(grid[0])        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        num_islands = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    num_islands += 1
                    que = deque([(i,j)])
                    while que:
                        r,c = que.popleft()
                        if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1":
                            grid[r][c] = "0"
                            for dr, dc in directions:
                                que.append([r+dr, c+dc])
        return num_islands

        
        # DFS approach
        # rows = len(grid)
        # cols = len(grid[0])
        # count = 0
        # def dfs(row, col):
        #     if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col]=="0":
        #         return
        #     grid[row][col] = "0"
        #     dfs(row+1, col)
        #     dfs(row-1, col)
        #     dfs(row, col+1)
        #     dfs(row, col-1)
        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == "1":
        #             dfs(row, col)
        #             count += 1
        # return count