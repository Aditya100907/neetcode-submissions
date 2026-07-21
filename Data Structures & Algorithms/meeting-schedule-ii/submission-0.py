"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        h = []
        for interval in intervals:
            start, end = interval.start, interval.end
            if h and h[0] <= start:
                heapq.heapreplace(h, end)
            else:
                heapq.heappush(h, end)
        return len(h)