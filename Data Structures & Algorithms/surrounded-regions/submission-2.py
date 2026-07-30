class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        g = [[False] * len(board[0]) for _ in range(len(board))]

        def d(row, column):
            if row < 0 or column < 0 or row == len(board) or column == len(board[0]) or g[row][column] == True or board[row][column] == "X":
                return

            g[row][column] = True
            q.append((row, column))
        
        for i in range(len(board[0])):
            if board[0][i] == "O":
                q.append((0, i))

        for i in range(1, len(board) - 1):
            if board[i][0] == "O":
                q.append((i, 0))
            if board[i][len(board[0]) - 1] == "O":
                q.append((i, len(board[0]) - 1))
        
        for i in range(len(board[0])):
            if board[len(board) - 1][i] == "O":
                q.append((len(board) - 1, i))
        
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                row = curr[0]
                column = curr[1]
                g[row][column] = True
                d(row + 1, column)
                d(row - 1, column)
                d(row, column + 1)
                d(row, column - 1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if g[i][j] == False and board[i][j] == "O":
                    board[i][j] = "X"

                