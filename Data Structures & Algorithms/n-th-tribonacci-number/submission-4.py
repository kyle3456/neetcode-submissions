class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        d = [0, 1, 1]
        for i in range(2, n):
            if i + 1 == n:
                return sum(d)
            second = d[1]
            third = d[2]
            total = sum(d)
            d[0] = second
            d[1] = third
            d[2] = total