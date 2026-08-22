class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if curr < 0:
                curr = max(nums[i], curr)
            else:
                curr += nums[i]
            res = max(res, curr)
        return res