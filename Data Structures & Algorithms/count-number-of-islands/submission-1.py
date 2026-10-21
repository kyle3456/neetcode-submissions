class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        chosen = [[False] * len(grid[0]) for _ in range(len(grid))]

        def find(i, j):
            chosen[i][j] = True
            directions = [[0, 1], [0, -1], [1,0], [-1, 0]]
            for x, y in directions:
                if x + i >= 0 and x + i < len(grid) and y + j >= 0 and y + j < len(grid[0]) and grid[x+i][y+j] == "1" and chosen[x+i][y+j] == False:
                    find(x+i, y+j)

        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and chosen[i][j] == False:
                    num += 1
                    find(i, j)
        
        return num