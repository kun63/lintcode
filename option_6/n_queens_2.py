class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
        self.opt = {}
        def is_vaild(curr, l):
            index = len(l)
            for i in range(len(l)):
                diff = i + 1
                temp = {curr+diff,curr-diff}
                if l[i] in temp:
                    return False
            return True
                
        def dfs(l):
            if str(l) in self.opt:
                return self.opt[str(l)]
            if len(l) == 1:
                return [l]
            outcome = []
            for i in range(len(l)):
                temp_list = l[:]
                temp = temp_list.pop(i)
                rest = dfs(temp_list)
                for r in rest:
                    # if temp+1 == r[0] or temp-1 == r[0]:
                    #     continue
                    if is_vaild(temp,r):
                        outcome.append([temp]+r)
            self.opt[str(l)] = outcome
            return outcome
        def transf_chessboard(list_dfs):
            outcome = []
            for l in list_dfs:
                temp = []
                for i in l:
                    t = ['.']*n
                    t[i] = 'Q'
                    temp.append(''.join(t))
                outcome.append(temp)
            return outcome
        return len(dfs([x for x in range(n)]))



if __name__ == "__main__":
    print(Solution().totalNQueens(10))