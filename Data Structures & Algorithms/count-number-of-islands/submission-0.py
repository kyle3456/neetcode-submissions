class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        g = [[False] * len(grid[0]) for _ in range(len(grid))]
        n = 0

        def dfs(r, c):
            if r == -1 or c == -1:
                return
            if r == len(grid) or c == len(grid[0]):
                return
            if grid[r][c] == "0" or grid[r][c] == True:
                return
            grid[r][c] = True
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)  

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and g[i][j] == False:
                    dfs(i, j)
                    n += 1

        return n



