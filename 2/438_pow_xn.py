class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def _myPow(self, x, n):
        # write your code here
        if n == 0:
            return 1
        i = 0
        while n%2 == 0:
            i += 1
            n = n//2
        k = n
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
        
        if temp_k < 0:
            t = 1/t
        v = t
        for _ in range(i):
            v = v*v
        return v

    def myPow(self, x, n):
        # write your code here
        if n == 0:
            return 1
        binary = []
        negitive = 0
        if n < 0:
            negitive = -1
            if n < -100:
                return 0.00
            n = -n
        v = n
        while v != 0:
            binary.append(v % 2)
            v = v // 2
        
        bin_v = [x]
        t = x
        for _ in range(len(binary)-1):
            t = t * t
            bin_v.append(t)
        outcome = 1
        for i in range(len(binary)):
            temp = binary[i] * bin_v[i]
            if temp == 0:
                temp = 1
            outcome = outcome * temp
        if negitive == -1:
            outcome = 1/outcome
        return outcome


if __name__ == "__main__":
    print(Solution().myPow(2,-100))