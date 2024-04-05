class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
    
    def checkwin(self, player):
        n = self.n

        #horizontal
        for row in self.board:
            if len(set(row)) == 1 and row[0] != 0:
                return player
        
        # vertical
        for i in range(n):
            winset = set()
            for j in range(n):
                winset.add(self.board[j][i])
            if len(set(winset)) == 1 and self.board[0][i] != 0:
                return player
            
        # + diagonal
        winset = set()
        for i in range(n):
            winset.add(self.board[i][i])
        if len(set(winset)) == 1 and self.board[0][0] != 0:
            return player
        
        winset = set()
        for i in range(n):
            winset.add(self.board[i][n-1-i])
        if len(set(winset)) == 1 and self.board[0][n-1] != 0:
            return player
        return 0

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        return self.checkwin(player)


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)