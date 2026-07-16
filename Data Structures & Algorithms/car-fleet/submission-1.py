class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #[[7,1],[4,2],[1,2],[0,1]]
        #time = 4.5
        #stack = [3,4.5,10]
        #cnt = 3
        cars = sorted(zip(position, speed), reverse = True)
        stack = []
        cnt = len(speed)
        for pos, spd in cars:
            time = (target - pos)/spd

            if stack and stack[-1] >= time:
                cnt -= 1
            
            else: stack.append(time)

        return cnt

