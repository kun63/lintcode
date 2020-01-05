class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # write your code here
        if not grid:
            return -1
        import collections
        start = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start.add((i,j))
        visited = collections.defaultdict(set)
        distance =  collections.defaultdict(int)
        step = -1
        reach = collections.defaultdict(set)
        curr = collections.defaultdict(list)
        for s in start:
            curr[s].append(s)
            visited[s].add(s)
        flag = 1
        best_distance = float('inf')
        while flag:
            flag = 0
            step += 1
            for s in start:
                curr_direction = curr[s][:]
                curr[s].clear()
                for x,y in curr_direction:
                    if s not in reach[(x,y)]:
                        reach[(x,y)].add(s)
                        if grid[x][y] == 0:
                            distance[(x,y)] += step
                        if len(reach[(x,y)]) == len(start) and distance[(x,y)] < best_distance:
                            best_distance = distance[(x,y)]
                            best_postion = (x,y)
                    directions = {(x+1,y),(x-1,y),(x,y+1),(x,y-1)}
                    for a,b in directions:
                        if a in range(len(grid)) and b in range(len(grid[0])) and (a,b) not in visited[s] and grid[a][b] != 1 and grid[a][b] != 2:
                            curr[s].append((a,b))
                            visited[s].add((a,b))
                if curr[s] != []:
                    flag = 1
        if best_distance == float('inf'):
            return -1
        else:
            # print(best_postion)
            return best_distance

if __name__ == "__main__":
    print(Solution().shortestDistance([[0,1,0],[1,0,1],[0,1,0]]))
