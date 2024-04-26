class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        size = len(grid)
        prev_row = [0] * size
        for row in grid:
            curr_row = [0] * size
            for i, n in enumerate(row):
                curr_row[i] = n
                if prev_row[0:i] + prev_row[i+1:size]:
                    curr_row[i] += min(prev_row[0:i] + prev_row[i+1:size])
            prev_row = curr_row
        return min(prev_row)