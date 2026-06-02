class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(r, c, index):
            if index >= len(word):
                return True
            
            if r >= len(board) or r < 0 or c >= len(board[r]) or c < 0 or (r, c) in visited:
                return False
            
            if board[r][c] != word[index]:
                return False
            
            visited.add((r, c))
            found =  dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1) or dfs(r, c + 1, index + 1) or dfs(r, c - 1, index + 1)
            visited.remove((r, c))
            return found        
        for r in range(0, len(board)):
            for c in range(0, len(board[r])):
                #visited.clear()
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        
        return False
