class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        # 5#HELLO5#WORLD
        for i in strs:
            s += str(len(i)) + "#" + i
        return s
    
    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        while i < len(s):
            j = i
            #j = 7
            #length = 5
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            l.append(s[j + 1:length + j + 1])
            i = length + j + 1
        return l
