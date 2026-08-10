class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def d(openN, closeN):
            if closeN == openN == n:
                res.append("".join(curr))
                return

            if openN < n:
                curr.append("(")
                d(openN + 1, closeN)
                curr.pop()
            
            if closeN < openN:
                curr.append(")")
                d(openN, closeN + 1)
                curr.pop()

            return
        
        d(0, 0)
        return res