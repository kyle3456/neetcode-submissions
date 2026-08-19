class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {n}
        while n != 1:
            s = str(n)
            new = 0
            for digit in s:
                d = int(digit)
                new += d**2
            if new in visited:
                return False
            visited.add(new)
            n = new
        return True
        