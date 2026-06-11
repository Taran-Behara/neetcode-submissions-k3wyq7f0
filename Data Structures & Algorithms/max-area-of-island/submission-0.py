class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(r, c):
            if (r, c) in visited:
                return 0
            visited.add((r, c))
            up = 0
            down = 0
            right = 0
            left = 0

            if r - 1 >= 0 and grid[r - 1][c] != 0:
                up = dfs(r - 1, c)
            
            if r + 1 < len(grid) and grid[r + 1][c] != 0:
                down = dfs(r + 1, c)
            
            if c + 1 < len(grid[r]) and grid[r][c + 1] != 0:
                right = dfs(r, c + 1)
            
            if c - 1 >= 0 and grid[r][c - 1] != 0:
                left = dfs(r, c - 1)
            
            return 1 + up + down + right + left

        maxi = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxi = max(maxi, dfs(i, j))
        
        return maxi