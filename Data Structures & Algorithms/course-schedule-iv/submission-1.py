class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        reachable = [[False] * numCourses for _ in range(numCourses)]

        for pre, course in prerequisites:
            reachable[pre][course] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                if reachable[i][k]:
                    for j in range(numCourses):
                        if reachable[k][j]:
                            reachable[i][j] = True
            
        return [reachable[u][v] for u, v in queries]