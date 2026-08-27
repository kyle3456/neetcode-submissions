class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        d = defaultdict(list)

        for fro, to, cost in edges:
            d[fro].append([cost, to])
        
        h = [[0, src]]
        heapq.heapify(h)
        res = {}

        while h:
            cost, fro = heapq.heappop(h)
            if fro not in res:
                res[fro] = cost

                for new_cost, new_to in d[fro]:
                    heapq.heappush(h, [new_cost + cost, new_to])

        for i in range(n):
            if i not in res:
                res[i] = -1
        
        return res