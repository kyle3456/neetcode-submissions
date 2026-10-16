class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
         s = []
         res = [0] * len(temperatures)
         for i in range(len(temperatures)):
            if len(s) == 0 or temperatures[i] <= s[-1][0]:
                s.append((temperatures[i], i))
            elif temperatures[i] > s[-1][0]:
                while len(s) != 0 and temperatures[i] > s[-1][0]:
                    temp, ind = s.pop()
                    res[ind] = i - ind
                s.append((temperatures[i],i))
            
         return res