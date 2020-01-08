class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        if nums == []:
            return -1
        i = 0
        j = 0
        sum = nums[0]
        curr_len = float('inf')
        while j < len(nums):
            if sum >= s:
                curr_len = min(curr_len,j-i+1)
                sum -= nums[i]
                i += 1
                if i>j:
                    j = i
            else:
                if j < len(nums)-1:
                    j += 1
                    sum += nums[j]
                else:
                    j += 1
        if curr_len == float('inf'):
            return -1
        return curr_len

if __name__ == '__main__':
    print(Solution().minimumSize([2,3,1,10,4,3],7))