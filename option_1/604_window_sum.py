class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        if nums == []:
            return []
        outcome = []
        sum_ = 0
        for num in nums[:k]:
            sum_ += num
        outcome.append(sum_)
        for n in range(k,len(nums)):
            sum_ -= nums[n-k]
            sum_ += nums[n]
            outcome.append(sum_)
        return outcome

if __name__ == "__main__":
    print(Solution().winSum([1,2,7,8,5],3))
