class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        
        r = [[] for _ in range(len(nums) + 1)]

        for num, val in d.items():
            r[val].append(num)

        res = []
        s = 0
        for i in range(len(r) - 1, 0, -1):
            for j in range(len(r[i])):
                res.append(r[i][j])
                s += 1
                if s == k:
                    return res



        
        
