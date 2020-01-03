"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        # write your code here
        def find(point):
            # x,y = point
            if point not in self.point:
                self.point[point] = point
                self.num_islands += 1
                return point
            if self.point[point] != point:
                self.point[point] = find(self.point[point])
            return self.point[point]
        
        def union(c):
            point_1, point_2 = c
            point_1 = find(point_1)
            point_2 = find(point_2)
            if point_1 == point_2:
                return
            point_1, point_2 = sorted([point_1,point_2])
            self.point[point_1] = point_2
            self.num_islands -= 1
            

            





        if operators == []:
            return []
        if n == 0 and m == 0:
            return []
        self.point = {}
        
        self.num_islands = 0
        result = []
        import copy
        sea = []
        for _ in range(n):
            sea.append([0]*m)

        visited = set()


        for x,y in operators:
            if (x,y) in visited:
                result.append(self.num_islands)
                continue
            visited.add((x,y))
        # for o in operators:
        #     x, y = o.x, o.y
            sea[x][y] = 1
            directions = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
            flag = 0
            connection = []
            for a,b in directions:
                if a>=0 and b>=0 and a<=n-1 and b<=m-1 and sea[a][b] == 1:
                    flag = 1
                    connection.append(((x,y),(a,b)))
            if flag == 0:
                self.num_islands += 1
                self.point[(x,y)] = (x,y)
            else:
                for c in connection:
                    union(c)
            result.append(self.num_islands)
        return result

if __name__ == "__main__":
    print(Solution().numIslands2(3,3,[[0,0],[0,1],[2,2],[2,2]]))
    # print(Solution().numIslands2(2,2,[[0,0],[1,1],[1,0],[0,1]]))

