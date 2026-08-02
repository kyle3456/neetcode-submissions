class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        rob1 = 0
        rob2 = 0
        for i in range(len(nums) - 1):
            c = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = c
        
        rob11 = 0
        rob22 = 0
        for i in range(len(nums) - 1, 0, -1):
            cc = max(rob11 + nums[i], rob22)
            rob11 = rob22
            rob22 = cc
        
        return max(rob2, rob22)