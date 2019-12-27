class Solution:
    def partition(self, s: str):
        def palindrome(s):
            if len(s) == 1:
                return True
            l = len(s)
            if l%2 == 0:
                left = s[:l//2]
                right = s[l//2:]
                
            else:
                l = l-1
                left = s[:l//2]
                right = s[l//2+1:]
            right = list(right)
            right.reverse()
            right = ''.join(right)
            if left == right:
                return True
            else:
                return False
        def gen_palindrome(s):
            # if s == []:
            #     return []
            if len(s) == 1:
                return [[s]]

            l = len(s)
            outcome = []
            for i in range(1,l):
                left = s[:i]
                right = s[i:]
                if palindrome(left):
                    temp = gen_palindrome(right)
                    for t in temp:
                        outcome.append([left]+t)
            if len(s) != 1 and palindrome(s):
                outcome.append([s])
            return outcome
        # return palindrome(s)
        result = gen_palindrome(s)
        
        return result

if __name__ == "__main__":
    s = 'baa'
    print(Solution().partition(s))