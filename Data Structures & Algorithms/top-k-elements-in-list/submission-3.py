class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = defaultdict(int)
        for i in range(len(nums)):
            s[nums[i]] += 1

        d = [[] for _ in range(len(nums) + 1)]
        for key, value in s.items():
            d[value].append(key)
        res = []
        l = 0
        for i in range(len(nums), 0, -1):
            for j in range(len(d[i])):
                res.append(d[i][j])
                l += 1
            if l == k:
                return res