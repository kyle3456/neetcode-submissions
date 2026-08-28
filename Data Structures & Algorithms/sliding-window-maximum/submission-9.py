class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l = r = 0
        q = deque()
        res = []
        while r < len(nums):

            while q and q[-1][0] < nums[r]:
                q.pop()

            q.append((nums[r], r))

            if q[0][1] < l:
                q.popleft()

            if r - l + 1 == k:
                res.append(q[0][0])
                l += 1

            r += 1

        return res