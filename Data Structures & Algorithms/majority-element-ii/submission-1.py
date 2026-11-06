class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]] += 1
            if len(d) <= 2:
                continue
            new_d = defaultdict(int)
            for n,a in d.items():
                if a != 1:
                    new_d[n] = a - 1
            
            d = new_d
        res = []
        for n,a in d.items():
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        
        return res