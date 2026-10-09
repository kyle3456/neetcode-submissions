class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r = []
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            target = nums[i]
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                curr = nums[left] + nums[right]
                if target + curr == 0:
                    r.append([nums[left], nums[right], target])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    continue
                if target + curr > 0:
                    right -= 1
                elif target + curr < 0:
                    left += 1

        return r
            




