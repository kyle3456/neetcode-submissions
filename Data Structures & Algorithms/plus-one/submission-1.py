class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        all_9 = True
        for i in range(len(digits)):
            if digits[i] != 9:
                all_9 = False


        if all_9:
            r = []
            r.append(1)
            for i in range(len(digits)):
                r.append(0)
            
            return r
        if digits[0] >= 0:
            digits[len(digits) - 1] += 1
        else:
            digits[len(digits) - 1] -= 1

        for i in range(len(digits) - 1, -1, -1):
            if abs(digits[i]) == 10:
                digits[i] = 0
                if digits[i] >= 0:
                    digits[i - 1] += 1
                else:
                    digits[i - 1] -= 1
        
        return digits