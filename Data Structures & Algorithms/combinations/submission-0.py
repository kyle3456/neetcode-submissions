class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        t = []
        def dfs(curr, l):
            if l == k:
                res.append(t[:])
                return
            for i in range(curr, n + 1):
                t.append(i)
                dfs(i + 1, len(t))
                t.pop()
        dfs(1, 0)
        return res