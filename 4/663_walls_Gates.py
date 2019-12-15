import copy

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def _wallsAndGates(self, rooms):
        # write your code here
        def find_dis(i,j,entry,visited):
            # print(i,j)
            if (i,j) in visited:
                return -1
            else:
                visited.add((i,j))
            room = rooms[i][j]
            if room == -1:
                return -1
            elif room == 0:
                return 0
            else:
                entry_set = set([1,2,3,4])
                if entry != 0:
                    entry_set.remove(entry)
                out = []
                o = -1
                for e in entry_set:
                    if e == 1 and i != 0:
                        o = find_dis(i-1,j,3,visited)
                    elif e == 2 and j != 0:
                        o = find_dis(i,j-1,2,visited)
                    elif e == 3 and i != n-1:
                        o = find_dis(i+1,j,1,visited)
                    elif e == 4 and j != m-1:
                        o = find_dis(i,j+1,2,visited)
                    if o == 0:
                        return 1
                    if o != -1:
                        out.append(o)
                out = [x for x in out if x >= 0 and x < 2147483647]
                if len(out) == 0:
                    return 2147483647
                else:
                    return min(out)+1


        n = len(rooms)
        m = len(rooms[0])
        outcome = copy.deepcopy(rooms)


        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 2147483647:
                    visited = set()
                    temp = find_dis(i,j,0,visited)
                    outcome[i][j] = temp
                    # print(i,j,temp)
        
        for i in range(n):
            for j in range(m):
                if rooms[i][j] != outcome[i][j]:
                    rooms[i][j] = outcome[i][j]
        return


    def wallsAndGates(self, rooms):
        # write your code here
        def spread(i,j,v):
            if rooms[i][j] <= v:
                return
            else:
                rooms[i][j] = v + 1
                p = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
                for a,b in p:
                    # print(a,b)
                    if a>=0 and a<=m-1 and b>=0 and b<=n-1:
                        spread(a,b,v+1)
        m = len(rooms)
        n = len(rooms[0])
        start = [(i,j) for i in range(m) for j in range(n) if rooms[i][j] == 0]
        for i, j in start:
            spread(i,j,-1)


if __name__ == "__main__":
    x = [[2147483647,2147483647,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    # x = [[2147483647,2147483647,0,2147483647],[2147483647,2147483647,2147483647,2147483647]]
    Solution().wallsAndGates(x)
    for r in x:
        print(r)


def __wallsAndGates(self, rooms):
    # write your code here
    if len(rooms) == 0 or len(rooms[0]) == 0:
        return rooms
        
    m = len(rooms)
    n = len(rooms[0])
    
    import Queue
    queue = Queue.Queue()
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                queue.put((i, j))
                
    while not queue.empty():
        x, y = queue.get()
        
        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy
            
            if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or rooms[new_x][new_y] < rooms[x][y] + 1:
                continue
            
            rooms[new_x][new_y] = rooms[x][y] + 1
            queue.put((new_x, new_y))
            
    return rooms