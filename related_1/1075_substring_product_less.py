class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the number of subarrays where the product of all the elements in the subarray is less than k
    """
    def numSubarrayProductLessThanK(self, nums, k):
        # Write your code here
        start = 0
        end = 1
        outcome = 0
        if nums == []:
            return 0
        p_window = nums[0]
        while start < end and start <= len(nums)-1:
            # curr = nums[start:end]
            # p = 1
            
            # for c in curr:
            #     p = p*c
            if p_window < k:
                outcome += 1
                if end+1 <= len(nums):
                    end += 1
                    p_window = p_window * nums[end-1]
                    continue
            start += 1
            if start <= len(nums)-1:
                p_window = nums[start]
            end = start + 1
            
        return outcome

if __name__ == "__main__":
    print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6],100))
