class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        a = [amount + 1] * (amount + 1)
        a[0] = 0
        for needed in range(1,amount + 1):
            for c in coins:
                if needed - c >= 0:
                    a[needed] = min(a[needed], 1 + a[needed - c])
        
        if a[amount] == amount + 1:
            return -1
        return a[amount]
