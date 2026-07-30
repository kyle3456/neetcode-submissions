class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_deg = defaultdict(int)
        connect = defaultdict(list)
        for i in range(len(prerequisites)):
            totake, pre = prerequisites[i]
            in_deg[totake] += 1
            connect[pre].append(totake)

        q = deque()
        for course in range(numCourses):
            if in_deg[course] == 0:
                q.append(course)

        count = 0
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                count += 1
                for j in range(len(connect[curr])):
                    in_deg[connect[curr][j]] -= 1
                    if in_deg[connect[curr][j]] == 0:
                        q.append(connect[curr][j])
        
        if count == numCourses:
            return True
        else:
            return False
                



        


            

        

    