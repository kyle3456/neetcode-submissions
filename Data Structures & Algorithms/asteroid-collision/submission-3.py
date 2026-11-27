class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                t = True
                while t:
                    if len(stack) == 0:
                        stack.append(asteroids[i])
                        t = False
                        continue
                    n = len(stack) - 1
                    if stack[n] < 0:
                        stack.append(asteroids[i])
                        t = False
                        continue
                    if stack[n] > abs(asteroids[i]):
                        t = False
                    else:
                        if stack[n] == abs(asteroids[i]):
                            t = False
                        stack.pop()
            
        
        return stack