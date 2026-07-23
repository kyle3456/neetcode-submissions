class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = [1] * len(nums)

        p = 1
        for i in range(len(nums)):
            r[i] *= p
            p *= nums[i]

        s = 1
        for i in range(len(nums) - 1, -1, -1):
            r[i] *= s
            s *= nums[i]
        
        return r