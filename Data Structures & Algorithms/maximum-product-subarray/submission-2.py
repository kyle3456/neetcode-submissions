class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax = 1
        curMin = 1

        for i in range(len(nums)):
            curmax = curMax
            curmin = curMin
            curMax = max(curmax * nums[i], curmin * nums[i], nums[i])
            curMin = min(curmax * nums[i], curmin * nums[i], nums[i])

            res = max(curMax, res)
        return res