class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        # import queue
        # q = queue.Queue()
        m = len(grid)
        n = len(grid[0])
        zombie = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        q = []
        q = zombie[:]
        day = 0
        while len(q) != 0:
            # directions = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            temp = []
            for i,j in q:
                directions = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
                for a, b in directions:
                    if a>=0 and b>=0 and a<=m-1 and b<=n-1:
                        if grid[a][b] == 0:
                            grid[a][b] = 1
                            temp.append((a,b))
            day += 1
            q = temp[:]
        human = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 0]
        if len(human) != 0:
            return -1
        else:
            return day-1


if __name__ == "__main__":
    # x = [[0,1,2,0,0],[1,0,0,2,1],[0,1,0,0,0]]
    x = [[0,0,0],[0,0,0],[0,0,1]]
    print(Solution().zombie(x))
             
