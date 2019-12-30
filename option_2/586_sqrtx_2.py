class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        import collections
        accuary = collections.deque([1,0.1,0.01,0.001,0.0001,0.00001,0.000001,0.0000001,0.00000001,0.000000001,0.0000000001])
        curr = accuary.popleft()
        root = 0
        while accuary:
            if root**2 <x:
                root += curr
            else:
                root -= curr
                curr = accuary.popleft()
                root += curr
        # return float(str(root)[:10])
        str_root = str(root)
        outcome = float(str_root)
        dot = 9
        # print(str_root.find('.'))
        dot += str_root.find('.')
        # print(outcome[10])
        if int(str_root[dot]) >= 5:
            outcome += 0.00000001
        return float(str(outcome)[:dot])

    def _sqrt(self, x):
        # Write your code here
        result = 1.0;  
        while abs(result * result - x) > 1e-12:
            result = (result + x / result) / 2
        
        return result

if __name__ == "__main__":
    print(Solution().sqrt(1989891.012))
