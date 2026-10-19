class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        l = []
        def find(index, curr):
            if curr == target:
                res.append(l[:])
                return
            if curr > target:
                return
            for i in range(index, len(nums)):
                l.append(nums[i])
                curr += nums[i]
                find(i, curr)
                curr -= nums[i]
                l.pop()
            
        find(0,0)
        return res
