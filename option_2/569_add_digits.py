class Solution:
    """
    @param num: a non-negative integer
    @return: one digit
    """
    def addDigits(self, num):
        # write your code here
        if len(str(num)) == 1:
            return num
        outcome = 0
        for n in str(num):
            outcome += int(n)
        return self.addDigits(outcome)
