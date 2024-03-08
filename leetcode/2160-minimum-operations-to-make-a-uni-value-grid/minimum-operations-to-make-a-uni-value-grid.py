class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat_grid = sorted([i for l in grid for i in l])
        n = len(flat_grid)
        rem = flat_grid[0] % x
        for ele in flat_grid:
            if ele % x != rem:
                return -1

        idx = n // 2
        # print(idx, flat_grid[idx])
        
        def fx(idx):
            steps = 0
            for ele in flat_grid:
                l_num = max(ele, flat_grid[idx])
                s_num = min(ele, flat_grid[idx])
                # print(l_num, s_num, x)
                steps += ((l_num - s_num) // x)
            return steps

        start = idx
        min_steps = float(inf)
        while start >= 0:
            steps = fx(start)
            if steps < min_steps:
                min_steps = steps
                start -= 1
            else:
                break
        start = idx + 1
        while start < n:
            steps = fx(start)
            if steps < min_steps:
                min_steps = steps
                start += 1
            else:
                break
        
        return min_steps