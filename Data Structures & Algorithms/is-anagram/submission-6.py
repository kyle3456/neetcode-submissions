class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = defaultdict(int)
        two = defaultdict(int)
        for i in s:
            one[i] += 1
        for i in t:
            two[i] += 1
        return one == two
