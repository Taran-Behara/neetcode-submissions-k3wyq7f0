class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        currState = []
        for i in range(0, n):
            toAdd = ""
            for j in range(0, n):
                toAdd += "."
            currState.append(toAdd)
        
        def dfs(currState, currQ, resDiag1, resDiag2, resRow, resCol):
            # print(currState)
            # print(resPos)
            # print(resRow)
            # print(resCol)
            # print()
            if currQ == n:
                res.append(currState.copy())
                return
            
            row = currQ
            for col in range(0, len(currState[row])):
                diag1 = row - col
                diag2 = row + col
                if diag1 not in resDiag1 and diag2 not in resDiag2 and row not in resRow and col not in resCol:
                    curr = currState[row]
                    new = curr[0:col]
                    new += "Q"
                    new += curr[col + 1:len(curr)]
                    currState[row] = new
                    resRow.add(row)
                    resCol.add(col)
                    resDiag1.add(diag1)
                    resDiag2.add(diag2)
                    

                    dfs(currState, currQ + 1, resDiag1, resDiag2, resRow, resCol)
                    currState[row] = curr
                    resDiag1.remove(diag1)
                    resDiag2.remove(diag2)
                    resRow.remove(row)
                    resCol.remove(col)
        dfs(currState, 0, set(), set(), set(), set())
        return res