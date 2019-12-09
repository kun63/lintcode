class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        # write your code here
        if len(s) != len(t):
            return False
        dict_s = {}
        for c in s:
            if c in dict_s:
                dict_s[c] += 1
            else:
                dict_s[c] = 1
        for c in t:
            if c not in dict_s:
                return False
            if dict_s[c] == 0:
                return False
            dict_s[c] -= 1
        for c in dict_s:
            if dict_s[c] != 0:
                return False
        return True


if __name__ == "__main__":
    # print(Solution().anagram('ac','ab'))
    print(Solution().anagram("happy new year","n ahwryeypp ea"))

