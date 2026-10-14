class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        r = c = left = right = 0
        for i in range(len(nums) - 1):
            left = max(nums[i] + r, c)
            r = c
            c = left
        r = c = 0
        for i in range(1, len(nums)):
            right = max(nums[i] + r, c)
            r = c
            c = right

        return max(left, right)
