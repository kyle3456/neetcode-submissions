class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        l = len(prerequisites)
        d = defaultdict(list)
        in_deg = [0] * numCourses
        q = deque()
        number = 0
        res = []

        for i in range(l):
            in_deg[prerequisites[i][0]] += 1
            d[prerequisites[i][1]].append(prerequisites[i][0])
        
        for i in range(len(in_deg)):
            if in_deg[i] == 0:
                q.append(i)
                res.append(i)

        number += len(q)

        while q:
            for i in range(len(q)):
                totake = q.popleft()
                for m in d[totake]:
                    in_deg[m] -= 1
                    if in_deg[m] == 0:
                        q.append(m)
                        number += 1
                        res.append(m)
        
        if number == numCourses:
            return res
        else:
            return []

        
