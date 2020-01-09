class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        # if s == '' or s in {"()","{}","[]"}:
        #     return True
        vaild_str = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        stack = []
        for c in s:
            if c not in vaild_str:
                stack.append(c)
            elif stack and stack[-1] == vaild_str[c]:
                stack.pop()
            else:
                return False
        if stack != []:
            return False
        return True