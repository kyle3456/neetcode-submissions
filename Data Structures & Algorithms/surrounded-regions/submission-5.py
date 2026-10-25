class Solution:
    def solve(self, board: List[List[str]]) -> None:
        import sys
        sys.setrecursionlimit(100000)
        seen = [[True] * len(board[0]) for _ in range(len(board))]
        s = True
        current = []
        def find(x, y):
            nonlocal s
            current.append([x,y])
            seen[x][y] = False
            directions = [[-1,0],[1,0],[0,1],[0,-1]]
            for dx, dy in directions:
                Y = dy+y
                X = dx+x
                if X < 0 or X >= len(board) or Y < 0 or Y >= len(board[0]):
                    s = False
                elif seen[X][Y] and board[X][Y] == "O":
                    find(X,Y)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and seen[i][j]:
                    s = True
                    current = []
                    find(i, j)
                    if s:
                        for x,y in current:
                            board[x][y] = "X"

