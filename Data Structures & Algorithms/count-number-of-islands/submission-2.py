class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def dfs(r, c):
            if grid[r][c] == "0" or (r, c) in visited:
                return
            visited.add((r, c))
            if r - 1 >= 0:
                dfs(r - 1, c)

            if r + 1 < len(grid):
                dfs(r + 1, c)

            if c - 1 >= 0:
                dfs(r, c - 1)

            if c + 1 < len(grid[r]):
                dfs(r, c + 1)
        
        islands = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    dfs(i, j)
                print(visited)
        return islands
            

