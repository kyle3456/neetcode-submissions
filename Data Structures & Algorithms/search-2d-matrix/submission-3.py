class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1

        while l <= r:
            mid = int((l + r) / 2)
            row, col = divmod(mid, n)
            val = matrix[row][col]

            if val == target:
                return True

            if val < target:
                l = mid + 1
            
            else:
                r = mid - 1

        return False