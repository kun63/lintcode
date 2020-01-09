class Solution:
    """
    @param tokens: The Reverse Polish Notation
    @return: the value
    """
    def evalRPN(self, tokens):
        # write your code here
        if tokens == []:
            return 0
        stack = []
        operator = {'+','-','*','/'}
        for c in tokens:
            if c in operator:
                b = stack.pop()
                a = stack.pop()
                if c == '+':
                    stack.append(a+b)
                elif c == '-':
                    stack.append(a-b)
                elif c == '*':
                    stack.append(a*b)
                elif c == '/':
                    stack.append(int(a/b))
                continue
            else:
                stack.append(int(c))
        result = stack.pop()
        return result