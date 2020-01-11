class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def _longestIncreasingSubsequence(self, nums):
    
        # write your code here
        if not nums:
            return 0
        result = 1
        len_longest = 1
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                len_longest += 1
            else:
                result = max(result,len_longest)
                len_longest = 1    
        result = max(result,len_longest)
        return result
    def _longestIncreasingSubsequence(self, nums):
        l = len(nums)
        result = []
        for i in range(l):
            temp = []
            pre = nums[i]
            for x in nums[i:l+1]:
                if x >= pre:
                    temp.append(x)
                    pre = x
            result.append(len(temp))
        # result = [len([x for x in nums[i:len(nums)+1] if x >= nums[i]]) for i in range(len(nums))]
        return max(result)
    def longestIncreasingSubsequence(self, nums):
        longest = 0
        dp = {}
        for i in range(len(nums)):
            temp = []
            if i == 0:
                dp[i] = 1
            else:
                temp = [dp[j] for j in range(i) if nums[j] < nums[i]]
                if temp == []:
                    dp[i] = 1
                else:
                    dp[i] = max(temp) + 1
            # print(i,dp[i])
            # print(temp)
            if dp[i] > longest:
                longest = dp[i]

        return longest



if __name__ == "__main__":
    print(Solution().longestIncreasingSubsequence([4,2,4,5,3,7]))        
