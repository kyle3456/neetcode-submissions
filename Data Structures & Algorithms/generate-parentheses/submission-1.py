class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        curr = []

        def find(ope, close):
            if len(curr) == n * 2:
                res.append("".join(curr[:]))
                return
            elif ope == n:
                curr.append(")")
                find(ope, close + 1)
                curr.pop()
            else:
                curr.append("(")
                find(ope + 1, close)
                curr.pop()
                if close != ope:
                    curr.append(")")
                    find(ope, close + 1)
                    curr.pop()
        
        find(0, 0)
        return res