class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        d = {
            2 : ("a", "b", "c"),
            3 : ("d", "e", "f"),
            4 : ("g", "h", "i"),
            5 : ("j", "k", "l"),
            6 : ("m", "n", "o"),
            7 : ("p", "q", "r", "s"),
            8 : ("t", "u", "v"),
            9 : ("w", "x", "y", "z")
        }

        res = []
        c = []

        def m(curr):
            if curr == len(digits):
                res.append("".join(c))
                return

            CurrentNumber = int(digits[curr])
            for i in range(len(d[CurrentNumber])):
                c.append(d[CurrentNumber][i])
                m(curr + 1)
                c.pop()
        
            return

        m(0)
        return res
