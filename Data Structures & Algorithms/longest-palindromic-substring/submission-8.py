class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            b = 0
            r = ""
            while i - b >= 0 and i + b < len(s) and s[i - b] == s[i + b]:
                r = s[i - b:i + b + 1]
                b += 1
            if len(res) < len(r):
                res = r
            if i != 0 and s[i] == s[i - 1]:
                r = s[i - 1:i + 1]
                b = 0
                while i - b > 0 and i + b < len(s) and s[i - b - 1] == s[i + b]:
                    r = s[i - b - 1:i + b + 1]
                    b += 1
                if len(res) < len(r):
                    res = r

        return res
