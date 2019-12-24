class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        self.factor = [2,3,5,7]
        self.outcome = []
        def gen_factor(n):
            local_factor = []
            pre = []
            for f in self.factor:
                local_n = n
                while local_n % f == 0 and local_n != 1:
                    self.outcome.append(pre+[f,local_n/f])
                    pre.append(f)
                    n = local_n / f
                if local_n == 1:
                    break
            return local_factor
        def gen_list(list_factor):
            outcome = []
            for i in range(1,len(list_factor)):
                temp = 1
                for k in list_factor[i:]:
                    temp = temp*k
                list_temp = list_factor[:i]
                list_temp.append(temp)
                outcome.append(list_temp)
            return outcome

        def gen_factor_list(local_n,low):
            # for k in range(2,local_n):

            #     pre = []
            #     n = local_n
            #     if k > n / k:
            #         break
            #     if n % k == 0:
            #         for t in range(k,local_n):
                        
            #             while n % t == 0 and n != t:
            #                 self.outcome.append(pre+[t,int(n/t)])
            #                 pre.append(t)
            #                 n = n/t
            #             if n == 1 or n < t:
            #                 break
            local_list = []
            # for k in range(low,local_n+1):
            for k in range(low,local_n+1):

                pre = []
                n = local_n
                if k>100 and k > local_n**(1/2)+1:
                    print(k,local_n,local_n**(1/2)+1)
                    break
                
                if n == k:
                    local_list.append([k])
                    break
                if k > n / k:
                    continue
                if n % k == 0:
                    temp = gen_factor_list(int(n/k),k)
                    for t in temp:
                        local_list.append([k]+t)
                
            return local_list
                    # for t in range(k,local_n):
                        
                    #     while n % t == 0 and n != t:
                    #         self.outcome.append(pre+[t,int(n/t)])
                    #         pre.append(t)
                    #         n = n/t
                    #     if n == 1 or n < t:
                    #         break


        self.outcome = gen_factor_list(n,2)
        if self.outcome:
            self.outcome.pop()
        return self.outcome

if __name__ == "__main__":
    print(Solution().getFactors(12))