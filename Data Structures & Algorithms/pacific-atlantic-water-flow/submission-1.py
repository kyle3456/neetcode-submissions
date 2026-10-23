class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlanticq = deque()
        pacificq = deque()
        atlanticseen = [[True] * len(heights[0]) for _ in range(len(heights))]
        pacificseen = [[True] * len(heights[0]) for _ in range(len(heights))]

        for i in range(len(heights[0])):
            pacificq.append([0, i])
            atlanticq.append([len(heights) - 1, i])
            pacificseen[0][i] = False
            atlanticseen[len(heights) - 1][i] = False

        for i in range(len(heights)):
            pacificq.append([i, 0])
            atlanticq.append([i, len(heights[0]) - 1])
            pacificseen[i][0] = False
            atlanticseen[i][len(heights[0]) - 1] = False
        
        while atlanticq:
            for i in range(len(atlanticq)):
                x,y = atlanticq.popleft()
                directions = [[1, 0],[-1, 0], [0, 1], [0,-1]]
                for dx,dy in directions:
                    X = dx+x
                    Y = dy + y
                    if X >= 0 and X < len(heights) and Y >= 0 and Y < len(heights[0]) and heights[x][y] <= heights[X][Y] and atlanticseen[X][Y]:
                        atlanticq.append([X, Y])
                        atlanticseen[X][Y] = False

        while pacificq:
            for i in range(len(pacificq)):
                x,y = pacificq.popleft()
                directions = [[1, 0],[-1, 0], [0, 1], [0,-1]]
                for dx,dy in directions:
                    X = dx+x
                    Y = dy + y
                    if X >= 0 and X < len(heights) and Y >= 0 and Y < len(heights[0]) and heights[x][y] <= heights[X][Y] and pacificseen[X][Y]:
                        pacificq.append([X, Y])
                        pacificseen[X][Y] = False

        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if not atlanticseen[i][j] and not pacificseen[i][j]:
                    res.append([i,j])
        return res
