class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        s = set()
        for i in range(n):
            for j in range(n):
                if board[i][j] in s:
                    return False
                if board[i][j] != ".":
                    s.add(board[i][j])
            s = set()

        for i in range(n):
            for j in range(n):
                if board[j][i] in s:
                    return False
                if board[j][i] != ".":
                    s.add(board[j][i])
            s = set()
        
        i = 0
        j = 0
        for _ in range(3):
            for _ in range(3):
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] in s:
                            return False
                        if board[i + k][j + l] != ".":
                            s.add(board[i + k][j + l])
                j += 3
                s = set()
            j = 0
            i += 3

        return True





