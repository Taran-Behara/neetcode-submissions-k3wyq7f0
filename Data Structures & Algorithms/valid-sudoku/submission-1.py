class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsValid = True

        seen = set()
        for row in board:
            for char in row:
                if char in seen and char != ".":
                    rowsValid = False
                seen.add(char)
            seen.clear()

        colsValid = True
        for col in range(0, len(board[0])):
            for row in range(0, len(board)):
                char = board[row][col]
                if char in seen and char != ".":
                    colsValid = False
                seen.add(char)
            seen.clear()
        
        boxesValid = True
        
        leftCornerRow = 0
        leftCornerCol = 0
        
        while True:
            seen = set()
            for i in range(leftCornerRow, leftCornerRow + 3):
                for j in range(leftCornerCol, leftCornerCol + 3):
                    if board[i][j] in seen and board[i][j] != ".":
                        boxesValid = False
                    seen.add(board[i][j])
            seen.clear()

            if leftCornerCol == 6 and leftCornerRow == 6:
                break
            if leftCornerCol == 6:
                leftCornerRow = leftCornerRow + 3
                leftCornerCol = 0
            else:
                leftCornerCol = leftCornerCol + 3
        return rowsValid and colsValid and boxesValid