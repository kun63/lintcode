class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        if s == t:
            return False
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] == t[i]:
                    continue
                else:
                    s = list(s)
                    s.pop(i)
                    t = list(t)
                    t.pop(i)
                    if s == t:
                        return True
                    else:
                        return False
        else:
            if len(s) < len(t):
                s, t = t, s
            if len(s) != len(t) + 1:
                return False
            for i in range(len(t)):
                if s[i] == t[i]:
                    continue
                else:
                    s = list(s)
                    t = list(t)
                    t.insert(i, s[i])
                    if s == t:
                        return True
                    else:
                        return False
            return True

if __name__ == "__main__":
    print(Solution().isOneEditDistance('abd','acd'))