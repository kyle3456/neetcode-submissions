class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        h = [(0, k)]
        d = defaultdict(list)
        for i in times:
            source, target, time = i
            d[source].append((target, time, source))
        

        heapq.heapify((h))
        visited = set()
        while h:
            time, source = heapq.heappop(h)
            if source in visited:
                continue
            visited.add(source)
            if len(visited) == n:
                return time
            for i in d[source]:
                new_target, new_time, new_source = i
                heapq.heappush(h, (new_time + time, new_target))

        return -1
