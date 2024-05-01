class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        grid = [[] for _ in range(numRows)]

        index = 0
        step = 1
        for c in s:
            grid[index].append(c)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        
        res = ""
        for r in range(numRows):
            res += "".join(grid[r])
        return res