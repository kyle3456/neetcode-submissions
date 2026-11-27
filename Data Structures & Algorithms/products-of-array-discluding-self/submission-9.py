class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums[0]
        left = defaultdict(int)
        right = defaultdict(int)
        for i in range(len(nums)):
            if i == 0:
                left[i] = nums[i]
            else:
                left[i] = nums[i] * left[i - 1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right[i] = nums[i]
            else:
                right[i] = nums[i] * right[i + 1]
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(right[i + 1])
            elif i == len(nums) - 1:
                res.append(left[i - 1])
            else:
                res.append(right[i + 1] * left[i - 1])
        
        return res
        
