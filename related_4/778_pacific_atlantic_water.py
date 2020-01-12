class Solution:
    """
    @param matrix: the given matrix
    @return: The list of grid coordinates
    """
    def pacificAtlantic(self, matrix):
        # write your code here
        m = len(matrix)
        n = len(matrix[0])
        q_pacific = [(0,x) for x in range(n)]
        q_pacific.extend([(x,0) for x in range(m)])
        q_atlantic = [(m-1,x) for x in range(n)]
        q_atlantic.extend([(x,n-1) for x in range(m)])
        visited = set()
        pacific = set()
        pacific.update(q_pacific)
        atlantic = set()
        atlantic.update(q_atlantic)
        while q_pacific:
            for i in range(len(q_pacific)):
                (x,y) = q_pacific.pop(0)
                # visited.add([x,y])
                # directions = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
                directions = ((x+1,y),(x-1,y),(x,y+1),(x,y-1))
                next = []
                
                for a,b in directions:
                    if (a,b) not in visited and 0<=a<=m-1 and 0<=b<=n-1 and matrix[x][y] <= matrix[a][b]:
                        next.append((a,b))
                pacific.update(next)
                visited.update(next)
                q_pacific.extend(next)
        visited = set()
        print(pacific)
        while q_atlantic:
            for i in range(len(q_atlantic)):
                (x,y) = q_atlantic.pop(0)
                # visited.add([x,y])
                # directions = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
                directions = ((x+1,y),(x-1,y),(x,y+1),(x,y-1))
                next = []
                
                for a,b in directions:
                    if (a,b) not in visited and 0<=a<=m-1 and 0<=b<=n-1 and matrix[x][y] <= matrix[a][b]:
                        next.append((a,b))
                atlantic.update(next)
                visited.update(next)
                q_atlantic.extend(next)
        print(atlantic)
        return [[a,b] for a,b in pacific.intersection(atlantic)]

if __name__ == "__main__":
    a = [   [1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4]
        ]
    print(Solution().pacificAtlantic(a))