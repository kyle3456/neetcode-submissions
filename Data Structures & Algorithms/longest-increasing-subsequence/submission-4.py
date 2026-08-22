class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        d = [1] * len(nums)
        m = -1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    d[i] = max(d[i], d[j] + 1)
                    m = max(d[i], m)

        if m == -1:
            return 1
            
        return m