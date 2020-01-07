class Solution:
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """
    def _isScramble(self, s1, s2):
        # write your code here
        import collections
        self.opt = collections.defaultdict(list)
        def dfs(str):
            if str in self.opt:
                return self.opt[str]
            if len(str) == 1:
                self.opt[str] = [str]
                return self.opt[str]
            outcome = set()
            for i in range(len(str)-1):
                first = dfs(str[0:i+1])
                second = dfs(str[i+1:])
            # print([a+b for a in first for b in second])
                outcome.update([a+b for a in first for b in second])
                outcome.update([b+a for a in first for b in second])
            # outcome.remove(str)
            self.opt[str] = list(outcome)
            return self.opt[str]
        # return dfs(s1)
        for i in range(len(s1)):
            first = dfs(s1[0:i+1])
            if s2[0:i+1] not in first:
                continue
            elif i == len(s1)-1:
                return True
            
            second = dfs(s1[i+1:])
            outcome = set()
            outcome.update([a+b for a in first for b in second])
            outcome.update([b+a for a in first for b in second])
            if s2 in outcome:
                return True
        return False
    def isScramble(self, s1, s2, opt=None):
        if opt == None:
            opt = {}
        if tuple(sorted((s1,s2))) in opt:
            return opt[tuple(sorted((s1,s2)))]
        if s1 == s2:
            # opt[sorted((s1,s2))] = True
            return True
        if sorted(s1) != sorted(s2):
            # opt[sorted((s1,s2))] = False
            return False
        if len(s1) <= 3:
            opt[tuple(sorted((s1,s2)))] = True
            return True
        for i in range(len(s1)-1):
            a = s1[0:i+1]
            b = s1[i+1:]
            c = s2[0:i+1]
            d = s2[i+1:]
            k = len(s1) - i - 1
            c_ = s2[0:k]
            d_ = s2[k:]
            if (self.isScramble(a,c,opt) and self.isScramble(b,d,opt)) or (self.isScramble(a,d_,opt) and self.isScramble(b,c_,opt)):
                opt[tuple(sorted((s1,s2)))] = True
                return True
        return False
            



if __name__ == "__main__":
    print(Solution().isScramble("vsgqrxvxyojzuznigvosftggtjjcefwnnxsrrdnjntyadhkflthltidpwpnwxmgmgfnwftvdyonozuvdtbuuxzcwnmvkpqqggrxn","svqgxrxvoyzjzuinvgsotfggjtcjfenwxnrsdrjntnayhdfktllhitpdpwwnmxmgfgwntfdvoyonuzdvbtuuzxwcmnkvqpgqrgnx"))
    # print(Solution().isScramble('abc','bca'))
    # print(Solution()._isScramble('great','rgeat'))
