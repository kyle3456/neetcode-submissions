class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for i in sorted(count):
            n = count[i]
            if n > 0:
                for j in range(groupSize):
                    if count[i + j] < n:
                        return False
                    count[i + j] -= n
        
        return True
