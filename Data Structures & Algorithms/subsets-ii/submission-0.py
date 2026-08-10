class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curr = []
        res = []

        def d(node):
            res.append(curr[:])
            for i in range(node, len(nums)):
                if i > node and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                d(i + 1)
                curr.pop()

        d(0)
        
        return res



