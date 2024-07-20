class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r = len(rowSum)
        c = len(colSum)

        res = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                minVal = min(rowSum[i], colSum[j])
                res[i][j] = minVal
                rowSum[i] -= minVal
                colSum[j] -= minVal
        return res