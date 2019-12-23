class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        if digits = '':
            return []
        self.outcome = {}
        self.phone_number = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        def helper(str):
            if len(str) > 1:
                addon = helper(str[1:])
                result = []
                for a in self.phone_number[str[0]]:
                    for b in addon:
                        result.append(a+b)
                return result
            return self.phone_number[str]
        return helper(digits)


if __name__ == "__main__":
    print(Solution().letterCombinations('23'))