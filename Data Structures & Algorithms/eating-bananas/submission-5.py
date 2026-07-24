class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        r = []
        while left <= right:
            t = 0
            mid = (left + right) // 2
            for i in range(len(piles)):
                if piles[i] % mid != 0:
                    t += 1
                t += int(piles[i] / mid)
            if t <= h:
                r.append(mid)
                right = mid - 1
            else:
                left = mid + 1

        return min(r)
    