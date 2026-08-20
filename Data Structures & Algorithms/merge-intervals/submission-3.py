class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        res = []
        cur_start, cur_end = intervals[0]

        for i in range(1, n):
            
            if cur_end >= intervals[i][0]:
                cur_end = max(cur_end, intervals[i][1])
            else:
                res.append([cur_start, cur_end])
                cur_start, cur_end = intervals[i]

        res.append([cur_start, cur_end])

        return res
    


        
