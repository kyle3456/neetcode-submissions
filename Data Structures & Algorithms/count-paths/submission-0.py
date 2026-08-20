class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        grid[0][0] = 1


        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i > 0 and j > 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
                elif i == 0:
                    grid[i][j] = grid[i][j - 1]
                else:
                    grid[i][j] = grid[i - 1][j]
        
        return grid[m - 1][n - 1]


