class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        has = [[True] * len(grid[0]) for _ in range(len(grid))]

        def find(i, j, curr):
            curr += 1
            has[i][j] = False
            direction = [[0,1],[0,-1],[1,0],[-1,0]]
            for x,y in direction:
                if x + i >= 0 and x + i < len(grid) and y + j >= 0 and y + j < len(grid[0]) and has[x + i][y + j] and grid[x + i][y + j] == 1:
                    curr = find(x + i, y + j, curr)
            return curr



        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and has[i][j]:
                    curr = find(i, j, 0)
                    res = max(curr, res)
        
        return res