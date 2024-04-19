class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # DFS approach
        # rows = len(grid1)
        # cols = len(grid1[0])
        # count = 0
        # def dfs(row, col):
        #     if row < 0 or col < 0 or row >= rows or col >= cols or grid2[row][col]==0:
        #         return
        #     grid2[row][col] = 0
        #     dfs(row+1, col)
        #     dfs(row-1, col)
        #     dfs(row, col+1)
        #     dfs(row, col-1)

        # # remove all un-common sub-islands from grid 2    
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid2[r][c] == 1 and grid1[r][c] == 0:
        #             dfs(r, c)

        # # count the remaining islands on grid2
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid2[r][c] == 1:
        #             dfs(r, c)
        #             count += 1
        # return count


        # BFS approach
        ROWS, COLS = len(grid1), len(grid1[0])        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        num_islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    que = deque([(i,j)])
                    while que:
                        r,c = que.popleft()
                        if 0 <= r < ROWS and 0 <= c < COLS and grid2[r][c] == 1:
                            grid2[r][c] = 0
                            for dr, dc in directions:
                                que.append([r+dr, c+dc])
        for i in range(ROWS):
            for j in range(COLS):
                if grid1[i][j] == 1 and grid2[i][j] == 1:
                    num_islands += 1
                    que = deque([(i,j)])
                    while que:
                        r,c = que.popleft()
                        if 0 <= r < ROWS and 0 <= c < COLS and grid2[r][c] == 1 and grid1[r][c]==1:
                            grid2[r][c] = 0
                            for dr, dc in directions:
                                que.append([r+dr, c+dc])
        return num_islands