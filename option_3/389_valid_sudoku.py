class Solution:
    """
    @param board: the board
    @return: whether the Sudoku is valid
    """
    def isValidSudoku(self, board):
        # write your code here
        for row in board:
            for i in row:
                if i == '.':
                    continue
                if row.count(i) != 1:
                # if ''.join(row).count(i) != 1:
                    return False
        for i in range(9):
            visited = set()
            for row in board:
                if row[i] == '.':
                    continue
                if row[i] in visited:
                    return False
                else:
                    visited.add(row[i])
        index = [[0,1,2],[3,4,5],[6,7,8]]
        for a in index:
            for b in index:
                visited = set()
                for x in a:
                    for y in b:
                        if board[x][y] == '.':
                            continue
                        if board[x][y] in visited:
                            return False
                        else:
                            visited.add(board[x][y])
        return True
if __name__ == "__main__":
    print(Solution().isValidSudoku(["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]))