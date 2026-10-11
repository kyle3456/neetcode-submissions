class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        res = 0
        has = set()
        while right < len(s):
            if s[right] in has:
                while s[left] != s[right]:
                    has.remove(s[left])
                    left += 1
                left += 1
            else:
                has.add(s[right])

            right += 1
            res = max(res, right - left)

        return res