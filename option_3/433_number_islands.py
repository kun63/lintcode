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
        self.visited = set()
        self.width = len(grid[0])
        self.length = len(grid)
        def bfs(x,y):
            self.visited.add((x,y))
            directions = {(x-1,y),(x+1,y),(x,y-1),(x,y+1)}
            trash = set()
            for a, b in directions:
                if a<0 or b<0 or b>self.width-1 or a>self.length-1 or (a,b) in self.visited:
                    trash.add((a,b))
            for t in trash:
                directions.remove(t)
            for a, b in directions:
                if grid[a][b] == 1:
                    bfs(a,b)
        start = []
        for a in range(self.length):
            for b in range(self.width):
                if grid[a][b] == 1:
                    start.append((a,b))
        while start:
            x,y = start.pop()
            if (x,y) in self.visited:
                continue
            bfs(x,y)
            self.count += 1
        return self.count

if __name__ == "__main__":
    print(Solution().numIslands([
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]))


