class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True

        stack = []
        closeToOpen = { 
        ")" : "(", 
        "]" : "[", 
        "}" : "{"
        }

        for c in s:
            if c in closeToOpen:
                if stack == []:
                    return False
                if stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
    
        if stack == []:
            return True
        return False