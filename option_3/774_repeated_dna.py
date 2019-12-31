class Solution:
    """
    @param s: a string represent DNA sequences
    @return: all the 10-letter-long sequences 
    """
    def findRepeatedDna(self, s):
        # write your code here
        visited = set()
        result = set()
        for i in range(len(s)-9):
            curr = s[i:i+10]
            if curr in visited:
                continue
            if s.count(curr) > 1 or s.find(curr) != s.rfind(curr):
                visited.add(curr)
                result.add(curr)
            else:
                visited.add(curr)
        return list(result)

if __name__ == "__main__":
    print(Solution().findRepeatedDna('AAAAAAAAAAA'))
