class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        i = 0
        j = len(num)-1
        while i <= j:
            if (num[i],num[j]) in {('6','9'),('9','6')}:
                i += 1
                j -= 1
                continue
            elif num[i] == num[j] and num[i] in {'1','0','8'}:
                i += 1
                j -= 1
                continue
            else:
                return False
        return True
                