class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        if len(s) == 0:
            return 0
        def num(s, n=None, opt=None):
            if opt == None:
                opt = {0:1, 1:1}
                n = len(s)
            if n in opt:
                return opt[n]
            num_1 = int(s[n-1])
            num_2 = int(s[n-1]) + 10*int(s[n-2])
            num_1_way = 0
            num_2_way = 0
            if num_1 != 0:
                num_1_way = num(s,n-1,opt)
            elif num_2 == 0:
                opt[n-1] = 0
                opt[n] = 0
                return 0
            if num_2 < 27 and int(s[n-2]) != 0:
                num_2_way = num(s,n-2,opt)
            opt[n] = num_1_way + num_2_way
            return opt[n]
        if int(s) == 0:
            return 0
        return num(s)

if __name__ == "__main__":
    print(Solution().numDecodings('10'))
    print(Solution().numDecodings('101'))
    print(Solution().numDecodings('19261001'))