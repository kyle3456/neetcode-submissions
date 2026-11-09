class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        l = r = 0
        while r < len(nums):
            if nums[r] in s:
                return True
            s.add(nums[r])
            if len(s) > k:
                s.remove(nums[l])
                l += 1
            r += 1

        return False
            
                
