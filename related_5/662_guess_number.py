"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""


class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        # Write your code here
        if n == 1:
            return 1
        if Guess.guess(n) == 0:
            return n
        high = n
        low = 1
        
        while 1:
            g = low + (high - low)//2
            p = Guess.guess(g)
            if p == 1:
                low = g
            elif p == -1:
                high = g
            else:
                return g