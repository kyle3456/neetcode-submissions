class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        g = [[False] * len(grid[0]) for _ in range(len(grid))]
        z = 0
        def dfs(r, c, area):
            
            if r < 0 or c < 0:
                return area
            
            if r == len(grid) or c == len(grid[0]):
                return area

            if g[r][c] == True or grid[r][c] == 0:
                return area

            area += 1
            g[r][c] = True

            area = dfs(r + 1, c, area)
            area = dfs(r - 1, c, area)
            area = dfs(r, c + 1, area)
            area = dfs(r, c - 1, area)

            return area


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if g[i][j] == False and grid[i][j] == 1:
                    area = dfs(i,j,0)
                    z = max(z, area)
        
        return z


