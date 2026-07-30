class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = [[False] * len(heights[0]) for _ in range(len(heights))]
        atlantic = [[False] * len(heights[0]) for _ in range(len(heights))]

        def dfs_pacific(row, column, val):
            if row < 0 or column < 0 or row == len(heights) or column == len(heights[0]) or val > heights[row][column] or pacific[row][column] == True:
                return

            pacific[row][column] = True
            val = heights[row][column]
            dfs_pacific(row + 1, column, val)
            dfs_pacific(row - 1, column, val)
            dfs_pacific(row, column + 1, val)
            dfs_pacific(row, column - 1, val)


        def dfs_atlantic(row, column, val):
            if row < 0 or column < 0 or row == len(heights) or column == len(heights[0]) or val > heights[row][column] or atlantic[row][column] == True:
                return

            atlantic[row][column] = True
            val = heights[row][column]
            dfs_atlantic(row + 1, column, val)
            dfs_atlantic(row - 1, column, val)
            dfs_atlantic(row, column + 1, val)
            dfs_atlantic(row, column - 1, val)

        for i in range(len(heights[0])):
            val = heights[0][i]
            dfs_pacific(0, i, val)

        for i in range(1, len(heights)):
            val = heights[i][0]
            dfs_pacific(i, 0, val)

        for i in range(len(heights[0])):
            val = heights[len(heights) - 1][i]
            dfs_atlantic(len(heights) - 1, i, val)

        for i in range(0, len(heights) - 1):
            val = heights[i][len(heights[0]) - 1]
            dfs_atlantic(i, len(heights[0]) - 1, val)
        
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if atlantic[i][j] and pacific[i][j]:
                    res.append([i, j])
        
        return res
                


