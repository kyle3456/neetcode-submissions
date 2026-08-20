"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in range(len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            time.append((start, True))
            time.append((end, False))
        
        time.sort()
        res = 0
        count = 0
        for i in range(len(time)):
            cur_time, which = time[i]
            if which:
                count += 1
                res = max(res, count)
            else:
                count -= 1
        return res