class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = -1
        y = -1
        z = -1
        t = 0
        for i in range(len(triplets)):
            if target[0] < triplets[i][0] or target[1] < triplets[i][1] or target[2] < triplets[i][2]:
                t += 1
                continue
            x = triplets[i][0]
            y = triplets[i][1]
            z = triplets[i][2]
            break
        
        for i in range(t + 1, len(triplets)):
            if target[0] < triplets[i][0] or target[1] < triplets[i][1] or target[2] < triplets[i][2]:
                continue
            x = max(triplets[i][0], x)
            y = max(triplets[i][1], y)
            z = max(triplets[i][2], z)

        if x == target[0] and y == target[1] and z == target[2]:
            return True
        return False