class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
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

if __name__ == "__main__":
    x = ["XXXX","XOOX","XOOX","XOXX"]
    Solution().surroundedRegions(x)
    for e in x:
        print(e)
                 
