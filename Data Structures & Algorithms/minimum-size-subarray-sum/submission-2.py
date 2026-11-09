class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        l = r = total = 0
        curr = 1
        res = 1000
        while r < len(nums):
            total += nums[r]
            while total >= target:
                if total >= target:
                    res = min(curr, res)
                curr -= 1
                total -= nums[l]
                l += 1

            r += 1
            curr += 1
        
        return res