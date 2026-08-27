class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

            d = defaultdict(list)
            for source, dst, cost in edges:
                d[source].append([dst, cost])
            
            q = deque()
            q.append([src, 0])
            res = {}
            for i in range(n):
                res[i] = -1
            res[src] = 0

            while q:
                src, cst = q.popleft()
                for dst, cost in d[src]:
                    already_cost = float('inf')

                    if res[dst] != -1:
                        already_cost = res[dst]
                    
                    if already_cost > cst + cost:
                        q.append((dst, cst + cost))
                        res[dst] = cst + cost

            return res

        

                    
            
