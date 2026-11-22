class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return True
        q = deque()
        d = defaultdict(list)
        s = {edges[0][0]}
        for i in range(len(edges)):
            x, y = edges[i]
            d[x].append(y)
            d[y].append(x)
        
        q.append((edges[0][0], None))

        while q:
            for i in range(len(q)):
                node, before = q.popleft()
                for curr in d[node]:
                    if curr == before:
                        continue
                    if curr in s:
                        return False
                    s.add(curr)
                    q.append((curr, node))
        if len(s) != n:
            return False
        return True



