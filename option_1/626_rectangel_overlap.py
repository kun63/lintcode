"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param l1: top-left coordinate of first rectangle
    @param r1: bottom-right coordinate of first rectangle
    @param l2: top-left coordinate of second rectangle
    @param r2: bottom-right coordinate of second rectangle
    @return: true if they are overlap or false
    """
    

    def doOverlap(self, l1, r1, l2, r2):
        (_, a), (b, _) = sorted([sorted([l1.x,r1.x]), sorted([l2.x, r2.x)]])
        print(a,b)
        if a >= b:
            (_, a), (b, _) = sorted([sorted([l1.y,r1.y]), sorted([l2.y, r2.y)]])
            print(a,b)
            if a >= b:
                return True

if __name__ == "__main__":
    print(Solution().doOverlap([0,8],[8,0],[6,6],[10,0]))



