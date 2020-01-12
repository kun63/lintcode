class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1,-1]
        l = 0
        r = len(A)
        
        while l + 1 < r:
            mid = (l+r)//2
            if A[mid] < target:
                l = mid
            else:
                r = mid
        if A[r] == target:
            start = r
        else:
            return [-1,-1]
        if r == len(A)-1 or A[r+1] != target:
            return [start,start]
        
        l = 0
        r = len(A)
        
        while l + 1 < r:
            mid = (l+r)//2
            if A[mid] <= target:
                l = mid
            else:
                r = mid
        if A[r] == target:
            return [start,r]
        else:
            return [start,l]