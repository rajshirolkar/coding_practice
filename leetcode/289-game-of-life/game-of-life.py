class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
            """
            Do not return anything, modify board in-place instead.
            """
            rows = len(board)
            cols = len(board[0])
            for row in range(rows):
                for col in range(cols):
                    live_neighbors = 0
                    for i in range(max(0, row-1), min(rows, row+2)):
                        for j in range(max(0, col-1), min(cols, col+2)):
                            live_neighbors += board[i][j] & 1
                    if live_neighbors == 3 or live_neighbors - board[row][col] == 3:
                        board[row][col] |= 2
            for row in range(rows):
                for col in range(cols):
                    board[row][col] >>= 1
            return board