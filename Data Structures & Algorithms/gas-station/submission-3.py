class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        curr = 0
        worst = float('inf')
        worst_index = 0
        for i in range(len(gas)):
            curr += gas[i] - cost[i]
            if curr < worst:
                worst = curr
                worst_index = i

        if worst_index == len(gas) - 1:
            return 0
        return worst_index + 1
      
