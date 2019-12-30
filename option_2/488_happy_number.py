class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        # write your code here
        visited = set()
        num = n
        
        while num != 1:
            curr = 0
            for i in str(num):
                curr += int(i)**2
            if curr in visited:
                return False
            visited.add(curr)
            num = curr
        return True

if __name__ == "__main__":
    print(Solution().isHappy(19))