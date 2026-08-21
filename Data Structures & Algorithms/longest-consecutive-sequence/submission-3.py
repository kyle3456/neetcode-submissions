class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0
        for i in range(len(nums)):
            curr = nums[i]
            if not mp[curr]:
                mp[curr] = mp[curr - 1] + mp[curr + 1] + 1
                mp[curr + mp[curr + 1]] = mp[curr]
                mp[curr - mp[curr - 1]] = mp[curr]
                res = max(res, mp[curr])
        return res
