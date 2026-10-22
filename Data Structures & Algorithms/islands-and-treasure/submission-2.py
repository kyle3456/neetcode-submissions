class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i, j])
        
        time = 1
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dx, dy in directions:
                    if dx + x >= 0 and dx + x < len(grid) and dy + y >= 0 and dy + y < len(grid[0]) and grid[dx + x][dy + y] == INF:
                        grid[dx + x][dy + y] = time
                        q.append([dx + x, dy+y])
                
            time += 1