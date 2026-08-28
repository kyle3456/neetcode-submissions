class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curr = []
        for i in range(k):
            curr.append((-nums[i], i))
        
        heapq.heapify(curr)
        res = [-curr[0][0]]
        l = 0

        for i in range(k, len(nums)):
            l += 1
            heapq.heappush(curr, (-nums[i], i))
            while curr[0][1] < l:
                heapq.heappop(curr)
            res.append(-curr[0][0])
        
        return res
