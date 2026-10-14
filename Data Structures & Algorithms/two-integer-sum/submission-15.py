class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        s = set()
        for i in range(len(nums)):
            need = target - nums[i]
            if need in s:
                return [d[need], i]
            s.add(nums[i])
            d[nums[i]] = i