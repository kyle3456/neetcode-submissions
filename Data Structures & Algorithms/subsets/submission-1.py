class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = []
        res = []
        def find(curr):
            res.append(l[:])
            if curr == len(nums):
                return
            for i in range(curr, len(nums)):
                l.append(nums[i])
                find(i + 1)
                l.pop()

        find(0)
        return res