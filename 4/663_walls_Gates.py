class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        def find_dis(i,j,entry):
            if rooms[i][j] == -1:
                return -1

        n = len(rooms)
        m = len(rooms[0])
        for i in range(n):
            for j in range(m):
                if rooms[i][j] >= 2147483647:
                    rooms[i][j] == find_dis(i,j)