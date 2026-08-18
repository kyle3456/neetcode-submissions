class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rank = [1] * (n + 1)
        par = [i for i in range(n + 1)]

        def find(node):
            if par[node] == node:
                return node
            return find(par[node])
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return True
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return False
        
        for n1, n2 in edges:
            if union(n1, n2):
                return [n1, n2]
