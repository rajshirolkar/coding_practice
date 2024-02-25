class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        # Create a copy of the board to store the next state
        next_state = [[0 for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                # Check all eight neighbors
                for i in range(max(0, row-1), min(rows, row+2)):
                    for j in range(max(0, col-1), min(cols, col+2)):
                        if i == row and j == col:
                            continue  # Skip the cell itself
                        if board[i][j] == 1:
                            live_neighbors += 1
                # Apply the Game of Life rules to determine the next state
                if board[row][col] == 1 and live_neighbors in [2, 3]:
                    next_state[row][col] = 1  # Cell remains alive
                elif board[row][col] == 0 and live_neighbors == 3:
                    next_state[row][col] = 1  # Cell becomes alive

        # Update the original board with the next state
        for row in range(rows):
            for col in range(cols):
                board[row][col] = next_state[row][col]