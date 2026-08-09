class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        b = [[False] * len(board[0]) for _ in range(len(board))]
    

        def dfs(i, j, NextLetter):
            if NextLetter == len(word):
                return True

            if i > 0 and board[i - 1][j] == word[NextLetter] and b[i - 1][j] == False:
                b[i - 1][j] = True
                if dfs(i - 1, j, NextLetter + 1):
                    return True
                b[i - 1][j] = False

            if i != len(board) - 1 and board[i + 1][j] == word[NextLetter] and b[i + 1][j] == False:
                b[i + 1][j] = True
                if dfs(i + 1, j, NextLetter + 1):
                    return True
                b[i + 1][j] = False

            if j > 0 and board[i][j - 1] == word[NextLetter] and b[i][j - 1] == False:
                b[i][j - 1] = True
                if dfs(i, j - 1, NextLetter + 1):
                    return True
                b[i][j - 1] = False
            
            if j < len(board[0]) - 1 and board[i][j + 1] == word[NextLetter] and b[i][j + 1] == False:
                b[i][j + 1] = True
                if dfs(i, j + 1, NextLetter + 1):
                    return True
                b[i][j + 1] = False

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    b[i][j] = True
                    if dfs(i, j, 1):
                        return True
                b[i][j] = False
        return False