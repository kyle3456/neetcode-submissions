class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        curr = 0
        t = set()
        m = 0
        for _ in range(len(s)):
            while s[curr] in t:
                t.remove(s[l])
                l += 1
            t.add(s[curr])
            m = max(m, curr - l + 1)
            curr += 1
        
        return m