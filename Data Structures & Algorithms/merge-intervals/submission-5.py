class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        if len(intervals) == 0:
            return res
        cur_start, cur_end = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= cur_end:
                cur_end = max(cur_end, intervals[i][1])
            else:
                res.append([cur_start, cur_end])
                cur_start, cur_end = intervals[i]
        
        res.append([cur_start, cur_end])
        return res