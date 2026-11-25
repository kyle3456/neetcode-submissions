class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for i in range(len(strs[0])):
            curr = strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != curr:
                    return "".join(res)

            res.append(strs[0][i])
                    
        return "".join(res)