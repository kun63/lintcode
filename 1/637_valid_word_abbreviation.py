class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        # write your code here
        s_i = 0
        a_i = 0
        while a_i <= len(abbr)-1:
            if abbr[a_i].isalpha():
                if abbr[a_i] == word[s_i]:
                    a_i += 1
                    s_i += 1
                else:
                    return False
            else:
                num = abbr[a_i]
                if int(abbr[a_i]) == 0:
                    return False
                while a_i+1 <= len(abbr)-1 and abbr[a_i+1].isdigit():
                    a_i += 1
                    num += abbr[a_i]
                num = int(num)
                a_i += 1
                s_i += num
                if s_i > len(word):
                    return False

        return True

if __name__ == "__main__":
    s = Solution()
    print(s.validWordAbbreviation('a','1'))
    print(s.validWordAbbreviation('aa','a2'))