"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here

        if len(intervals) == 0:
            return []
        _intervals = []
        for i in intervals:
            _intervals.append((i.start,i.end))
        _intervals.sort()
        print(_intervals)
        output = []
        s,e = _intervals[0]
        current_s = s
        current_e = e
        for s,e in _intervals:
            
            if s <= current_e:
                if e > current_e:
                    current_e = e
            else:
                x = Interval(current_s, current_e)
                output.append(x)
                current_s = s
                current_e = e
        x = Interval(current_s, current_e)
        output.append(x)
        return output

if __name__ == "__main__":
    intervals = [Interval(2,3),Interval(4,5),Interval(6,7),Interval(8,9),Interval(1,10)]
    s = Solution()
    for i in s.merge(intervals):
        print(i.start,i.end)
