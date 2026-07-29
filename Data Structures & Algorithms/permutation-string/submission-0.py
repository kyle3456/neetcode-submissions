class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        d = defaultdict(int)
        for i in range(len(s1)):
            d[s1[i]] += 1

        left = 0
        for right in range(len(s2)):

            if s2[right] in d.keys():
                d[s2[right]] -= 1

            if right - left + 1 > len(s1):
                if s2[left] in d.keys():
                    d[s2[left]] += 1
                left += 1
            
            is_done = True
            for i in range(len(s1)):
                if d[s1[i]] != 0:
                    is_done = False
            
            if is_done:
                return True
        
        return False

