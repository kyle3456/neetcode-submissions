class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        visited = set()
        res = 0
        q = deque()
        for i in range(len(edges)):
            d[edges[i][0]].append(edges[i][1])
            d[edges[i][1]].append(edges[i][0])
        
        for i in range(len(edges)):
            curr = edges[i][0]
            if curr not in visited:
                q.append(curr)
                visited.add(curr)
                while q:
                    current = q.popleft()
                    for k in d[current]:
                        if k in visited:
                            continue
                        visited.add(k)
                        q.append(k)
                
                res += 1
        remainder = n - len(visited)
        return res + remainder
            

            
