class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        t = 99999999
        while left <= right:
            mid = (left + right) //2
            if t > nums[mid]:
                t = nums[mid]

            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return t