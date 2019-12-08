class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        if nums == []:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower)+'->'+str(upper)]
        start = nums[0]
        l = 0
        r = 0
        outcome = []
        if start == lower+1:
            outcome.append(str(lower))
        elif start > lower+1:
            temp = str(lower) + '->' + str(start-1)
            outcome.append(temp)

        end = nums[-1]
        if end < upper:
            nums.append(upper+1)
        for i in range(len(nums)-1):
            l = nums[i]
            r = nums[i+1]
            if l < r-1:
                l += 1
                r -= 1
                if l == r:
                    outcome.append(str(l))
                else:
                    temp = str(l) + '->' + str(r)
                    outcome.append(temp)
        return outcome
