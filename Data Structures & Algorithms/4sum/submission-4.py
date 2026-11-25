class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        seen = set()
        for i in range(len(nums) - 3):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            d = set()
            for j in range(i + 1, len(nums) - 2):
                if nums[j] in d:
                    continue
                d.add(nums[j])

                lo = j + 1
                hi = len(nums) - 1
                while lo < hi:

                    s = nums[lo] + nums[hi] + nums[i] + nums[j]

                    if s == target:
                        res.append([nums[i], nums[j], nums[lo], nums[hi]])

                        while lo < hi and nums[lo] == nums[lo + 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi - 1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    
                    elif s < target:
                        lo += 1
                    else:
                        hi -= 1
                    
                
        return res
                    
