class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        s = 0
        res = -float('inf')
        for i in range(len(nums)):
            if s + nums[i] >= 0:
                s += nums[i]
                res = max(s, res)
            else:
                s = 0
                res = max(nums[i], res)
        
        return res