class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        # import collections
        if len(s) < 2:
            return len(s)
        start = 0
        end = 0
        # curr = collections.deque()
        curr = set()
        longest = 0
        while end <= len(s) - 1:
            while end <= len(s) - 1 and s[end] not in curr:
                curr.add(s[end])
                if len(curr) > longest:
                    longest = len(curr)
                if end <= len(s)-1:
                    end += 1
            curr.remove(s[start])
            start += 1

        return longest

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring('abcabcbb'))