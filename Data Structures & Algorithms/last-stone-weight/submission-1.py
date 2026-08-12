class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while(len(stones) >= 2):
            if stones[0] == stones[1]:
                heapq.heappop(stones)
                heapq.heappop(stones)
            else:
                t = heapq.heappop(stones)
                z = heapq.heappop(stones)
                t += abs(z)
                heapq.heappush(stones, t)
        if len(stones) == 0:
            return 0
        return abs(stones[0])