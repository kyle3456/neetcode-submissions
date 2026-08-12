class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for i in range(len(points)):

            t = math.sqrt(points[i][0]**2 + points[i][1]**2)
    
            heapq.heappush(heap, (-t, [points[i][0], points[i][1]]))
            
            while len(heap) > k:
                r = heapq.heappop(heap)
    

        s = []
        for i in range(k):
            s.append(heap[i][1])
            
        return s
            

            
        


    