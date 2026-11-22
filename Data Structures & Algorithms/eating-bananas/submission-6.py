class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return -1
        m = max(piles)
        
        l = 1
        r = m
        ret = float("INF")
        while l <= r:
            center = (l + r)//2
            res = 0
            for i in range(len(piles)):
                if center >= piles[i]:
                    res += 1
                else:
                    res += int(math.ceil(piles[i] / center))
            if res <= h:
                ret = center
                r = center - 1
            else:
                l = center + 1
    
        return ret
            





