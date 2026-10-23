class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i, j])
                if grid[i][j] == 1:
                    total += 1
        if total == 0:
            return 0
        t = 0
        n = True
        while q:
            F = True
            for i in range(len(q)):
                x, y = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0,-1]]
                for dx,dy in directions:
                    if dx + x >= 0 and dx+x < len(grid) and dy + y >= 0 and dy + y < len(grid[0]) and grid[dx + x][dy + y] == 1:
                        if F:
                            t += 1
                            F = False
                            n = False
                        total -= 1
                        grid[dx + x][dy + y] = 2
                        q.append([dx+x, dy+y])
                        
                if n:
                    t -= 1
        if total != 0:
            return -1
        
        return t