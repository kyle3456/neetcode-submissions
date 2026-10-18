class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        heapq.heapify(h)

        for x,y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(h, (distance, [x, y]))
        
        res = []
        for i in range(k):
            distance, l = heapq.heappop(h)
            res.append(l)
        
        return res