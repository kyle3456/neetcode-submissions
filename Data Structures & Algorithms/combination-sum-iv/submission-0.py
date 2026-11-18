class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        d = defaultdict(int)
        d[0] = 1
        for i in range(1, target + 1):
            for j in range(len(nums)):
                need = i - nums[j]
                if need < 0:
                    break
                d[i] += d[need]
        
        return d[target]
                    
