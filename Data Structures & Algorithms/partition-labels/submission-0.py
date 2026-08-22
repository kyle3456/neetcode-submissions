class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(int)
        for i in range(len(s)):
            d[s[i]] += 1

        res = []
        count = 0
        seen = set()
        for i in range(len(s)):
            d[s[i]] -= 1
            count += 1

            if s[i] not in seen:
                seen.add(s[i])

            if d[s[i]] == 0:
                seen.remove(s[i])

            if d[s[i]] == 0 and len(seen) == 0:
                res.append(count)
                count = 0
        
        return res