class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    def groupAnagrams(self, strs):
        # write your code here
        if strs == []:
            return []
        import collections
        ana = collections.defaultdict(list)
        for s in strs:
            ana[str(sorted(list(s)))].append(s)
        outcome = []
        for k in ana:
            outcome.append(ana[k])
        return outcome

if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))