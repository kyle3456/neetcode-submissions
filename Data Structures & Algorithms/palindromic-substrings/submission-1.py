class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):

            b = 0
            while i - b >= 0 and i + b < len(s) and s[i - b] == s[i + b]:
                b += 1
                res += 1
            
            if i > 0 and s[i] == s[i - 1]:
                b = 0
                while i - b > 0 and i + b < len(s) and s[i - b - 1] == s[i + b]:
                    b +=1
                    res += 1

        
        return res