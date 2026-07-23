class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeros = 0
        t = 1
        r = []
        for i in nums:
            if i == 0:
                num_zeros += 1
            else:
                t *= i
        if num_zeros >= 2:
            r = [0] * len(nums)
            return r
        if num_zeros == 1:
            for i in nums:
                if i == 0:
                    r.append(t)
                else:
                    r.append(0)
        else:
            for i in nums:
                r.append(int(t / i))
        return r

