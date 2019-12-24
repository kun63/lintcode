class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        palindrome = {}
        length = 0
        flag = 0
        for c in list(s):
            if c in palindrome:
                palindrome[c] += 1
            else:
                palindrome[c] = 1

        for p in palindrome:
            if palindrome[p] % 2 == 0:
                length += palindrome[p]
            elif palindrome[p] > 1:
                flag = 1
                length += palindrome[p] - 1
            else:
                flag = 1
        if flag == 1:
            length += 1
        print(palindrome)
        return length
if __name__ == "__main__":
    print(Solution().longestPalindrome('abccccdd'))