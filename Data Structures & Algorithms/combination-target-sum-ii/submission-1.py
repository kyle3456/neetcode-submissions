class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        l = []
        res = []
        candidates.sort()
        def find(index, curr):
            if curr == target:
                res.append(l[:])
                return
            elif curr > target:
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i - 1] == candidates[i]:
                    continue
                l.append(candidates[i])
                curr += candidates[i]
                find(i + 1, curr)
                curr -= candidates[i]
                l.pop()
        
        find(0,0)
        return res