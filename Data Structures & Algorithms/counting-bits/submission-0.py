class Solution:
    def countBits(self, n: int) -> List[int]:

        nums = [0] * (n + 1)

        for i in range(n + 1):
            curr = i
            while i:
                nums[curr] += i % 2
                i = i // 2
        return nums

    