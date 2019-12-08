"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        party = [x for x in range(n)]
        candidate = set(party)
        trash = []
        for c in candidate:
            for t in party:
                if c != t and Celebrity.knows(c,t):
                    trash.append(c)
                    break
        for t in trash:
            candidate.remove(t)
        if len(candidate) == 0:
            return -1
        trash = []
        for c in candidate:
            for p in party:
                if c != p and Celebrity.knows(p,c) == False:
                    trash.append(c)
                    break
        for t in trash:
            candidate.remove(t)
        if len(candidate) == 0:
            return -1
        else:
            return candidate.pop()