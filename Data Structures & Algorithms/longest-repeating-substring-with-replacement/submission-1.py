class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr = 0
        c = defaultdict(int)
        left = 0
        maxx = 0
        for right in range(len(s)):
            c[s[right]] += 1
                
            curr = max(curr, c[s[right]])
            
            while right - left + 1 > curr + k:
                c[s[left]] -= 1
                left += 1

            maxx = max(maxx, right - left + 1)
        return maxx