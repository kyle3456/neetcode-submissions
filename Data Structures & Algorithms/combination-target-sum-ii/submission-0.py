class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        r = []
        res = []
        candidates.sort()

        def look(node, needed):
            if needed == 0:
                res.append(r[:])
                return
            if needed < 0:
                return
            for i in range(node, len(candidates)):
                if i > node and candidates[i] == candidates[i - 1]:
                    continue
                r.append(candidates[i])
                look(i + 1, needed - candidates[i])
                r.pop()



        look(0, target)
        return res


    