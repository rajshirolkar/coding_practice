class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Dynamix Programming solution
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * (COLS+1) for _  in range(ROWS+1)]
        max_side = 0

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == '1':
                    down = dp[r+1][c]
                    right = dp[r][c+1]
                    curr = dp[r][c]
                    dp[r+1][c+1] = min(curr,down,right) + 1
                    max_side = max(max_side,dp[r+1][c+1])
        return max_side ** 2
        
        
        # Recursive Soltn
        # ROWS, COLS = len(matrix), len(matrix[0])
        # cache  = {}

        # def dfs(r,c):
        #     if r >= ROWS or c >= COLS:
        #         return 0
            
        #     if (r,c) not in cache:
        #         down = dfs(r+1,c)
        #         right = dfs(r,c+1)
        #         diag = dfs(r+1,c+1)

        #         if matrix[r][c] == '1':
        #             cache[(r,c)] = 1 + min(down, right, diag)
        #         else:
        #             cache[(r,c)] = 0
                
        #     return cache[(r,c)]
        
        # dfs(0,0)
        # return max(cache.values()) ** 2