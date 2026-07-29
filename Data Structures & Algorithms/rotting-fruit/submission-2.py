class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        total = 0
        s = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                    total += 1
                if grid[i][j] == 1:
                    s += 1

        if total == 0 and s > 0:
            return -1
        if total == 0:
            return 0
        def bfs(row, column):
            nonlocal s
            if row < 0 or column < 0 or row == len(grid) or column == len(grid[0]) or grid[row][column] == 0 or grid[row][column] == 2:
                return 1
            
            grid[row][column] = 2
            q.append((row, column))
            s -= 1
            return 0


        time = 0
        while q:
            r = 0
            t = len(q)
            for _ in range(len(q)):
                row, column = q.popleft()
                r += bfs(row + 1, column)
                r += bfs(row - 1, column)
                r += bfs(row, column + 1)
                r += bfs(row, column - 1)

            if r == t * 4 and s != 0:
                return -1
            time += 1

        return time - 1

