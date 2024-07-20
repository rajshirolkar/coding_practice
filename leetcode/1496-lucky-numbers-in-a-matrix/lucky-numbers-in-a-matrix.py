class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minRows = []
        maxCols = matrix[0]
        for r in range(len(matrix)):
            minRows.append(min(matrix[r]))
            for c in range(len(matrix[0])):
                maxCols[c] = max(matrix[r][c], maxCols[c])
        # print(minRows)
        # print(maxCols)
        res = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == minRows[r] == maxCols[c]:
                    res.append(matrix[r][c])
        return res