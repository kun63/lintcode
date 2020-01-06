class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if not dict and s == '':
            return True
        if not dict or s == '':
            return False
        max_len = max([len(x) for x in dict])
        def dfs(word):
            if word in dict:
                return True 
            if len(word) == 1 and word not in dict:
                return False
            for i in range(len(s)-1):
                if i > max_len:
                    return False
                if word[0:i+1] in dict:
                    return dfs(word[i+1:])
                # if dfs(word[0:i+1]):
                #     return True
            return False
        return dfs(s)

if __name__ == "__main__":
    print(Solution().wordBreak('',["lint", "cod"]))