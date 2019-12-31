class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid:
            return 0
        self.count = 0
        # self.visited = set()
        self.width = len(grid[0])
        self.length = len(grid)
        def bfs(x,y):
            import collections
            q = collections.deque([(x,y)])
            # self.visited.add((x,y))
            while q:
                x,y = q.popleft()
                directions = {(x-1,y),(x+1,y),(x,y-1),(x,y+1)}
                new = set()
                for a, b in directions:
                    if a<0 or b<0 or b>self.width-1 or a>self.length-1:
                        continue
                    else:
                        new.add((a,b))
                # for t in trash:
                #     directions.remove(t)
                for a, b in new:
                    if grid[a][b] == 1:
                        grid[a][b] = 0
                        q.append((a,b))
                        # self.visited.add((a,b))
        start = []
        for a in range(self.length):
            for b in range(self.width):
                if grid[a][b] == 1:
                    # start.append((a,b))
                    # if (a,b) in self.visited:
                    #     continue
                    grid[a][b] = 0
                    # self.visited.add((a,b))
                    bfs(a,b)
                    
                    self.count += 1
        # while start:
        #     x,y = start.pop()
            
        return self.count

if __name__ == "__main__":
    print(Solution().numIslands([
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]))


