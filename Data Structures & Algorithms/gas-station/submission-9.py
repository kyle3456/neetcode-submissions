class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = -1
        lowest = 0
        curr = 0
        total = 0
        for i in range(len(gas)):
            total = total - cost[i] + gas[i]
            if curr - cost[i] + gas[i] < 0:
                curr = curr - cost[i] + gas[i]
                if curr < lowest:
                    lowest = curr
                    start = i
            else:
                curr = 0
        if total < 0:
            return -1
        if start + 1 == len(gas):
            return 0
        return start + 1
        

            