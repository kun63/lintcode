class Solution:
    """
    @param s: the string s
    @return: the number of operations at least
    """
    def numberOfOperations(self, s):
        # Write your code here
        sum = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(s)//2):
            start = i
            end = len(s)-i-1
            sum += abs(alphabet.find(s[start]) - alphabet.find(s[end]))
        return sum

if __name__ == "__main__":
    print(Solution().numberOfOperations('abc'))