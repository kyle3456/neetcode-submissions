class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        memo = {}

        def dfs(t_index, s_index):

            if len(t) == t_index:
                return 1
            
            if len(s) == s_index:
                return 0
            
            if (t_index, s_index) in memo:
                return memo[(t_index, s_index)]
            
            count = 0
            for i in range(s_index, len(s)):
                if t[t_index] == s[i]:
                    count += dfs(t_index + 1, i + 1)
            
            memo[(t_index, s_index)] = count
            return count

        return dfs(0, 0)
        