class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        self.factor = [2,3,5,7]
        def gen_factor(n):
            for f in self.factor:
                
