class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(left, right):
            c = 0
            while right < len(s) and left > -1 and s[left] == s[right]:
                c += 1
                right += 1
                left -= 1
            return left + 1, right - 1
        
        r = 0
        end = 0
        start = 0
        for i in range(len(s)):
            left, right = expand(i, i)
            if end - start < right - left:
                end = right
                start = left
            
            left, right = expand(i, i + 1)
            if end - start < right - left:
                end = right
                start = left
        
        return s[start:end + 1]

            
            
                    

                