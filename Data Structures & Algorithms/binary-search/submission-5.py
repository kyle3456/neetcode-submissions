class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            a = (l + r) //2
            if nums[a] == target:
                return a
            if nums[a] > target:
                r = a - 1
            else:
                l = a + 1

        return -1