class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)
        for i in nums:
            heapq.heappush(h, -i)
        
        for i in range(k):
            curr = heapq.heappop(h)
        
        return -curr
