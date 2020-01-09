class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """
    def largestNumber(self, nums):
        # write your code here
        max_len = max([len(str(x)) for x in nums])
        for i in range(len(nums)):
            if len(str(nums[i])) < max_len:
                nums[i] = (nums[i], str(nums[i]) + (str(nums[i])[-1] * (max_len - len(str(nums[i])))))
            else:
                nums[i] = (nums[i], str(nums[i]))
        # print(nums)
        nums.sort(key = lambda x: (x[1],-len(str(x[0]))))
        nums.reverse()
        # print(nums)
        outcome = ''.join([str(x[0]) for x in nums])
        if outcome[0] == '0':
            # while outcome[0] == '0':
            #     outcome = outcome[1:]
            # if outcome == '':
            #     return 0
            return '0'
        return outcome

if __name__ == "__main__":
    print(Solution().largestNumber([1, 20, 23, 4, 8]))