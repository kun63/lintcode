"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        outcome = []
        left = newInterval.start
        right = newInterval.end
        flag = 0
        for i in range(len(intervals)):
            inter = intervals[i]
            s, e = inter.start, inter.end
            if s <= left <= e or s <= right <= e or left <= s <= right or left <= e <= right:
                left = min(s,left)
                right = max(right, e)
                flag = 1
            else:
                if flag:
                    outcome.append(Interval(left,right))
                    outcome.extend(intervals[i:])
                    return outcome
                else:
                    outcome.append(inter)
        
        outcome.append(Interval(left,right))
        outcome.sort()
        return outcome
