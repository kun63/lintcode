"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        if not grid:
            return -1
        length = len(grid)
        width = len(grid[0])
        import collections
        q = collections.deque([[source.x,source.y]])
        a, b = source.x, source.y
        grid[a][b] = 1
        step = 0
        while q:
            curr = []
            curr.extend(q)
            q.clear()
            for x,y in curr:
                directions = [(x + 1, y + 2),(x + 1, y - 2),(x - 1, y + 2),(x - 1, y - 2),(x + 2, y + 1),(x + 2, y - 1),(x - 2, y + 1),(x - 2, y - 1)]
                for a,b in directions:
                    if [a,b] == [destination.x,destination.y]:
                        return step+1
                    if a>=0 and b>=0 and a<=length-1 and b<=width-1 and grid[a][b] == 0:
                        grid[a][b] = 1
                        q.append([a,b])
            step += 1
        return -1

if __name__ == "__main__":
    print(Solution().shortestPath([[0,0,0],[0,0,0],[0,0,0]],[2, 0],[2, 2]))
