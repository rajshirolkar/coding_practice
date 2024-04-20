class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        q = deque()
        visit = set()

        def addRoom(r,c):
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                (r,c) in visit or rooms[r][c] == -1):
                return
            visit.add((r,c))
            q.append((r,c))
        
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rooms[r][c] = dist

                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist += 1
        