"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        rooms = 0
        ans = 0
        s = e = 0

        while s < n:
            if starts[s] < ends[e]:
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            ans = max(ans, rooms)
        
        return ans
