class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.horizontal = [0] * n
        self.vertical = [0] * n
        self.diag = 0
        self.antidiag = 0        

    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        move = 1 if player == 1 else -1
        self.horizontal[row] += move
        self.vertical[col] += move

        if row == col:
            self.diag += move
        if col == n - row - 1:
            self.antidiag += move
        
        if (abs(self.horizontal[row]) == n 
            or abs(self.vertical[col]) == n 
            or abs(self.diag) == n 
            or abs(self.antidiag) == n):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)


