class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = set()
        total = 0
        s.add(0)
        s.add(nums[0])
        for i in range(len(nums)):
            total += nums[i]
        if total % 2 != 0:
            return False
        total = total // 2
        for i in range(1, len(nums)):
            if total in s:
                return True
            curr = []
            for j in s:
                tmp = j + nums[i]
                curr.append(tmp)
            for j in curr:
                s.add(j)
        
        
        return False
    