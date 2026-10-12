class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for i in range(len(nums)):
            s.add(nums[i])
        
        starting = []
        for i in range(len(nums)):
            if nums[i] - 1 not in s:
                starting.append(nums[i])
        res = 0
        for i in range(len(starting)):
            curr = starting[i]
            r = 0
            while curr in s:
                r += 1
                curr += 1
            res = max(res, r)
        
        return res


        