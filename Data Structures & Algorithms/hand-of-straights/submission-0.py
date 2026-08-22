class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        d = defaultdict(int)
        for i in range(len(hand)):
            d[hand[i]] += 1
        
        hand.sort()
        for i in range(len(hand)):
            if d[hand[i]] > 0:
                for j in range(groupSize):
                    if j + i < len(hand):
                        if d[hand[i] + j] > 0:
                            d[hand[i] + j] -= 1
                        else:
                            return False
                    else:
                        return False
        
        return True
                