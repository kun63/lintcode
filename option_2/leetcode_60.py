class Solution:
    def getPermutation(self, n: int, k: int):
        self.count = 0
        self.result = None
        def dfs(visited, remain):
            if len(remain) == 1:
                self.count += 1
                if self.count == k:
                    curr = visited + remain
                    self.result = curr
                return
            for c in remain:
                if not self.result:
                    temp = remain.split(c)
                    dfs(visited+c,''.join(temp))
                else:
                    return
            return
        dfs('',''.join([str(x) for x in range(1,n+1)]))
        return self.result
if __name__ == "__main__":
    print(Solution().getPermutation(9,278621))