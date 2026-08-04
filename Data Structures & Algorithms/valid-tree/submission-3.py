class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m = 0
        d = defaultdict(list)
        s = set()

        def dfs(curr, prev):
            nonlocal m
            l = d[curr]
            for neighbor in l:
                if neighbor == prev:
                    continue
                if neighbor in s and neighbor != prev:
                    return False
                s.add(neighbor)
                m += 1
                if not dfs(neighbor, curr):
                    return False
            return True
            
            

        for i in range(len(edges)):
            d[edges[i][0]].append(edges[i][1])
            d[edges[i][1]].append(edges[i][0])

        
        return dfs(0, -1) and m == n - 1
        
