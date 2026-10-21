class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        s = set()
        res = []
        l = []
        def find():
            if len(l) == len(nums):
                res.append(l[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in s:
                    s.add(nums[i])
                    l.append(nums[i])
                    find()
                    l.pop()
                    s.remove(nums[i])

        find()
        return res