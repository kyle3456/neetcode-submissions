class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        heapq.heapify(nums)
        r = 1
        res = 1
        prev = None
        for i in range(len(nums)):
            curr = heapq.heappop(nums)
            if curr == prev:
                continue
            if prev is not None and prev + 1 == curr:
                res += 1
            else:
                r = max(res, r)
                res = 1
            prev = curr
        
        r = max(res, r)
        return r