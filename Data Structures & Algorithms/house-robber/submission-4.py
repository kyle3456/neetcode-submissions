class Solution:
    def rob(self, nums: List[int]) -> int:
        best = []
        
        for i in range(len(nums)):
            two_away = 0
            if i > 1:
                two_away = best[i - 2]
            one_away = 0
            if i > 0:
                one_away = best[i - 1]
            
            best.append(max(two_away + nums[i], one_away))
        
        return best[len(nums) - 1]
        