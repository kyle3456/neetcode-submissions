class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals

        n = True
        a = False
        c_start = newInterval[0]
        c_end = newInterval[1]
        res = []
        already_merged = False
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if end < c_start:
                res.append([start, end])
                if not a and n and ((i + 1) == len(intervals)):
                    res.append(newInterval)

            elif start > c_end:
                if n:
                    res.append(newInterval)
                    a = True
                    n = False
                res.append([start, end])
            else:
                if not already_merged:
                    already_merged = True
                else:
                    res.pop()
                c_start = min(c_start, start)
                c_end = max(c_end, end)
                res.append([c_start,c_end])
                n = False
        
        return res