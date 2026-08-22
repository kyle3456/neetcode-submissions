class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        r = 0
        l = 0
        farthest = 0
        while r < len(nums) - 1:
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1
            r = farthest
            count += 1
        return count