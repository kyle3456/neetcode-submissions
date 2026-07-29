class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        d = defaultdict(int)
        for i in range(len(s1)):
            d[s1[i]] += 1

        required = len(d)
        matches = 0
        left = 0
        for right in range(len(s2)):

            if s2[right] in d.keys():
                d[s2[right]] -= 1
                if d[s2[right]] == 0:
                    matches += 1

            if right - left + 1 > len(s1):
                if s2[left] in d.keys():
                    if d[s2[left]] == 0:
                        matches -= 1
                    d[s2[left]] += 1
                left += 1
            
            if matches == required:
                return True
        
        return False

