class Solution:
    """
    @param s: a string
    @return: it's index
    """
    def firstUniqChar(self, s):
        # write your code here
        visited = set()
        for i in range(len(s)):
            if s[i] in visited:
                continue
            count = s.count(s[i])
            visited.add(s[i])
            if count == 1:
                return s.find(s[i])
        return -1
