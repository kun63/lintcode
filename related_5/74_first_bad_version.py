#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        start = 1
        end = n
        if SVNRepo.isBadVersion(start):
            return 1
        if SVNRepo.isBadVersion(end) and not SVNRepo.isBadVersion(end-1):
            return n
        pre = True
        pre_number = n
        
        while 1:
            integer = start+(end-start)//2
            if SVNRepo.isBadVersion(integer):
                end = integer
                curr = True
            else:
                start = integer
                curr = False
            if (pre_number+1==integer or pre_number-1==integer) and curr != pre:
                return max([pre_number,integer])
            pre = curr
            pre_number = integer 