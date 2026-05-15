class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            
            while q:
                currNode = q.popleft()
                row = currNode[0]
                col = currNode[1]
                visited.add(currNode)
                if row - 1 >= 0 and grid[row - 1][col] == "1" and (row - 1, col) not in visited:
                    q.append((row - 1, col))
                
                if row + 1 < len(grid) and grid[row + 1][col] == "1" and (row + 1, col) not in visited:
                    q.append((row + 1, col))

                if col - 1 >= 0 and grid[row][col - 1] == "1" and (row, col - 1) not in visited:
                    q.append((row, col - 1))
                
                if col + 1 < len(grid[row]) and grid[row][col + 1] == "1" and (row, col + 1) not in visited:
                    q.append((row, col + 1))
            
            

            
            
            

        for r in range(0, len(grid)):
            for c in range(0, len(grid[r])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        


        return islands