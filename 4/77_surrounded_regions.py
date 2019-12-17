class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def _surroundedRegions(self, board):
        # write your code here
        if board == []:
            return []
        region = set()
        visited = set()
        m = len(board)
        n = len(board[0])
        start = [(i,j) for i in range(m) for j in range(n) if board[i][j] == 'O']
        for s in start:
            if s in visited:
                continue
            q = [s]
            flag = 0
            temp = set()
            while len(q) != 0:
                i,j = q.pop()
                # print(i,j)
                visited.add((i,j))
                temp.add((i,j))
                directions = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                for a, b in directions:
                    if a<0 or b<0 or a>m-1 or b>n-1:
                        flag = 1
                    elif board[a][b] == 'O':
                        if (a,b) not in visited:
                            q[:0] = [(a,b)]
                        visited.add((a,b))
                        temp.add((a,b))
                        
            if flag == 0:
                for t in temp:
                    region.add(t)
        # print(region)
        for i,j in region:
            board[i] = board[i][0:j]+'X'+board[i][j+1:]
            # board[i][j] = 'X'

    def surroundedRegions(self, board):
        # write your code here
        if board == []:
            return []
        m = len(board)
        n = len(board[0])
        visited = set()
        edge = set()
        for i in range(m):
            if i == 0 or i == m-1:
                for j in range(n):
                    if board[i][j] == 'O':
                        edge.add((i,j))
            else:
                if board[i][0] == 'O':
                    edge.add((i,0))
                if board[i][n-1] == 'O':
                    edge.add((i,n-1))
        q = list(edge)
        edge_visited = set()
        while len(q) != 0:
            i, j = q.pop()
            directions = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            visited.add((i,j))
            for a, b in directions:
                if (a,b) in visited:
                    continue
                if a>=0 and b>=0 and a<=m-1 and b<=n-1:
                    if board[a][b] == 'O':
                        # visited.add((a,b))
                        q[:0] = [(a,b)]
                        # if (a,b) in edge:
                        #     edge_visited.add((a,b))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if (i,j) in visited:
                        pass
                    else:
                        # board[i][j] = 'X'
                        board[i] = board[i][0:j]+'X'+board[i][j+1:]
        print(visited)
        return

if __name__ == "__main__":
    x = ["XXXX","XOOX","XOOX","XXXX"]
    Solution().surroundedRegions(x)
    for e in x:
        print(e)
                 
