class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for curr in strs:
            c = [0] * 26
            for letter in curr:
                 c[ord(letter) - ord("a")] += 1
            key = tuple(c)
            res[key].append(curr)
        
        return list(res.values())