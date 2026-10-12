class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z = 0
        res = []
        s = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                z += 1
                continue
            s *= nums[i]
            
        if z > 1:
            return [0] * len(nums)
        elif z == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(s)
                else:
                    res.append(0)
        else:
            for i in range(len(nums)):
                res.append(s // nums[i])
        
        return res