class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        starting = []
        for i in range(len(nums)):
            if nums[i] - 1 not in s and nums[i] + 1 in s:
                starting.append(nums[i])
        
        if len(starting) == 0:
            if len(nums) != 0:
                return 1
            else:
                return 0
        res = 0
        r = 0
        for i in range(len(starting)):
            res = 1
            curr = starting[i]
            while curr + 1 in s:
                res += 1
                curr = curr + 1
            r = max(r, res)

        return r
