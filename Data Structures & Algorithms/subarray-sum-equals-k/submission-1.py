class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        res = 0
        l = defaultdict(int)
        l[0] = 1
        for i in range(len(nums)):
            curr += nums[i]
            if l[curr - k] != 0:
                res += l[curr - k]
            l[curr] += 1
        return res