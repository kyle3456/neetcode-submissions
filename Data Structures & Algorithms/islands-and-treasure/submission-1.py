class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        g = [[False] * len(grid[0]) for _ in range(len(grid))]
        q = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
    
        def addRoom(r, c):
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] == -1 or g[r][c] or grid[r][c] == 0:
                return
            
            q.append((r, c))
            g[r][c] = True
        
        d = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = d

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)

            d += 1




