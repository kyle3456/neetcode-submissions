class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stars = []
        left = []
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == '*':
                stars.append(i)
            else:
                if len(left) != 0:
                    left.pop()
                else:
                    if len(stars) == 0:
                        return False
                    stars.pop() 

        if len(stars) < len(left):
            return False

        while left:
            curr_left = left.pop()
            curr_star = stars.pop()
            if curr_left > curr_star:
                return False
        
        return True