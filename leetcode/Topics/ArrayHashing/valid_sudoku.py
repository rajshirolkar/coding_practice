def isValidSudoku(self, board: List[List[str]]) -> bool:
    numDict = {f"{i}":False for i in range(1, 10)} 
    print(numDict)

    for i in range (0, 9):
        rowDict = numDict.copy()
        colDict = numDict.copy()
        if i%3 == 0:
            block1 = numDict.copy()
            block2 = numDict.copy()
            block3 = numDict.copy()
        for j in range(0,9):
            cell = board[i][j]
            if cell != ".":
                if rowDict[cell]:
                    return False
                rowDict[cell] = True
                if j<3:
                    if block1[cell]:
                        return False
                    block1[cell] = True
                if j>2 and j<6:
                    if block2[cell]:
                        return False
                    block2[cell] = True
                if j>5 and j<9:
                    if block3[cell]:
                        return False
                    block3[cell] = True
            cell = board[j][i]
            if cell != ".":
                if colDict[cell]:
                    return False
                colDict[cell] = True
    return True

 
# Example 1
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.   