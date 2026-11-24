class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        d = defaultdict(list)

        for i in range(len(prerequisites)):
            d[prerequisites[i][1]].append(prerequisites[i][0])
        
        r = defaultdict(set)
        def dfs(node):
            if node in r:
                return r[node]
            s = set()
            for i in d[node]:
                s.add(i)
                s |= dfs(i)
            r[node] = s
            return s

        res = []
        for i in range(len(queries)):
            dfs(queries[i][1])
            curr = r[queries[i][1]]
            if queries[i][0] in curr:
                res.append(True)
            else:
                res.append(False)
        return res