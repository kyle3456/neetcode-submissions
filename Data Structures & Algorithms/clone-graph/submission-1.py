"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        s = set()
        q = deque()
        q.append(node)
        s.add(node)
        if not node:
            return None
        t = Node(node.val)
        to = defaultdict(Node)
        to[node] = t
        while q:
            curr = q.popleft()
            for j in curr.neighbors:
                if j not in s:
                    s.add(j)
                    t = Node(j.val)
                    to[j] = t
                    q.append(j)
        s = set()
        q = deque()
        q.append(node)
        s.add(node)
        while q:
            curr = q.popleft()
            t = to[curr]
            for j in curr.neighbors:
                t.neighbors.append(to[j])
                if j not in s:
                    s.add(j)
                    q.append(j)
        return to[node]
        
        
                    
                    