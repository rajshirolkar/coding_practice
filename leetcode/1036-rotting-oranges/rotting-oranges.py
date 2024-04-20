class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def rot(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or ((r, c) in vis) or (grid[r][c] == 0) or (grid[r][c] == 2):
                return
            self.fresh_count -= 1
            q.append((r, c))
            vis.add((r, c))
        
        n = len(grid)
        m = len(grid[0])
        q = deque()
        vis = set()
        self.fresh_count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                    vis.add((i, j))
                if grid[i][j] == 1:
                    self.fresh_count += 1
        if len(q) == 0 and self.fresh_count == 0:
            return 0
        time = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                rot(r, c + 1)
                rot(r, c - 1)
                rot(r + 1, c)
                rot(r - 1, c)
            time += 1
        return time-1 if self.fresh_count == 0 else -1