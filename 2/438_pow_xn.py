class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n == 0:
            return 1
        i = 0
        while n%2 == 0:
            i += 1
            n = n//2
        k = n
        # print(i,k)

        # print(k)
        temp_k = 0
        if k < 0:
            temp_k = k
            k = -k
        if k == 0:
            t = x
        else:
            t = 1
            for _ in range(k):
                t = t*x
        # print('t', t)
        
        if temp_k < 0:
            t = 1/t
        # print('t', t)
        v = t
        # print(i)
        # if i == 0:
        #     v = 1
        # else:
        for _ in range(i):
            v = v*v
        
        
        return v


if __name__ == "__main__":
    print(Solution().myPow(8.84372,-5))