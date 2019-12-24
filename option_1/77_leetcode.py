class Solution:
    def combine(self, n: int, k: int):
        def helper(n, start, k):
            local_list = []
            if k == 1:
                return [[x] for x in range(start, n+1)]
            for t in range(start,n-k+2):
                temp = helper(n,t+1,k-1)
                for te in temp:
                    local_list.append([t]+te)
            return local_list
        return helper(n,1,k)

if __name__ == "__main__":
    print(Solution().combine(4,2))