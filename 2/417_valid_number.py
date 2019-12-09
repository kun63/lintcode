class Solution:
    """
    @param s: the string that represents a number
    @return: whether the string is a valid number
    """
    def isNumber(self, s):
        # write your code here
        def _isNumber(s):
            # if s.find(' ') != -1:
            #     return False
            if s == ' ':
                return False
            for i in range(len(s)):
                if s[i].isalpha():
                    if s[i] == 'e':
                        if s[i].count('e') != 1:
                            return False
                        else:
                            front, back = s.split('e')
                            if len(front) == 0 or len(back) == 0:
                                return False
                            return _isNumber(front) and _isNumber(back)
                    else:
                        return False
                elif s[i] == '.':
                    if s.count('.') != 1:
                        return False
                    else:
                        front, back = s.split('.')
                        if len(back) == 0 and len(front) == 0:
                                return False
                        return _isNumber(front) and _isNumber(back)
                elif s[i].isdigit():
                    continue
                elif s[i] == ' ':
                    temp = s[i:]
                    if s[:i] != '':
                        for x in range(len(temp)):
                            if temp[x] != ' ':
                                return False
                    else:
                        return _isNumber(s[i+1:])
                elif s[i] == '+' or s[i] == '-':
                    back = s[i:]
                    front = s[:i]
                    if front != '':
                        return False
                    else:
                        return _isNumber(s[i+1:])
                else:
                    return False
            return True
        return _isNumber(s)

if __name__ == "__main__":
    print(Solution().isNumber('0'))
    print(Solution().isNumber('2e10'))
    print(Solution().isNumber('e'))
    print(Solution().isNumber('.'))
    print(Solution().isNumber('.1'))
    print(Solution().isNumber('1.'))
    print(Solution().isNumber('1 '))
    print(Solution().isNumber(' 1'))
    print(Solution().isNumber(' '))
    print(Solution().isNumber('+.4'))
    