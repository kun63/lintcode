class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        # write your code here
        num_rev = str(num)
        num_rev = num_rev[::-1]
        if str(num) == num_rev:
            return True
        else:
            return False