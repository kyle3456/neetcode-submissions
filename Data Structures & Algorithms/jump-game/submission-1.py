class Solution:
    def canJump(self, nums: List[int]) -> bool:
        t = 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= t:
                t = 1
            else:
                t += 1
        
        if t == 1:
            return True
        return False