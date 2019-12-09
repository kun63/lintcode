class Solution:
    """
    @param s: a string
    @param p: a string
    @return: a list of index
    """
    def findAnagrams(self, s, p):
        # write your code here
        if len(s) < len(p):
            return []
        p = [c for c in p]
        p.sort()
        l = len(p)
        outcome = []
        previous = 0
        for i in range(len(s)-l+1):
            # print(i)
            if i>0 and i<len(s)-l and s[i-1] == s[i+l-1]:
                if previous == 1:
                    outcome.append(i)
                continue
            temp = s[i:i+l]
            temp = [c for c in temp]
            temp.sort()
            if temp == p:
                outcome.append(i)
                previous = 1
            else:
                previous = 0
        return outcome

if __name__ == "__main__":
    print(Solution().findAnagrams('cbaebabacd','abc'))
    