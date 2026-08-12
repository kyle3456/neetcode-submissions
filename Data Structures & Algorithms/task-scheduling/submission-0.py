class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        t = len(tasks)
        for i in range(len(tasks)):
            d[tasks[i]] -= 1
        l = list(d.values())
        
        heapq.heapify(l)
    
        time = 0
        q = deque()

        while t != 0:

            time += 1

            if len(l) != 0 and l[0] != 0:
                curr = heapq.heappop(l)
                t -= 1
                q.append((curr + 1, time + n))

            if q and q[0][1] == time:
                c = q.popleft()
                heapq.heappush(l, c[0])

        
        return time
