class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r = []
        res = []
        used = [False] * len(nums)

        def order():
            if len(nums) == len(r):
                res.append(r[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                r.append(nums[i])
                order()
                used[i] = False
                r.pop()

        order()

        return res