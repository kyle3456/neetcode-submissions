class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left  = sum(weights) // days
        right = sum(weights)        
        res = float("INF")
        while left <= right:
            load = (left + right) // 2       
            num = 0
            curr = 0
            for i in range(len(weights)):
                if curr + weights[i] > load:
                    curr = 0
                    num += 1  
                curr += weights[i]
            if num + 1 <= days and curr <= load and load >= max(weights):
                res = min(res, load)
                right = load - 1
            else:
                left = load + 1
        
        return res

            


