class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        num_set = set(num)
        visited = set()
        longest = 0
        for i in num:
            if i in visited:
                continue
            temp_len = 1
            l = i
            r = i
            while l-1 in num_set:
                visited.add(l-1)
                temp_len += 1
                l = l - 1
            while r+1 in num_set:
                visited.add(r+1)
                temp_len += 1
                r = r + 1
            if temp_len > longest:
                longest = temp_len


            # if i-1 in num_set and i+1 in num_set:
            #     temp_len = 3
            #     l = i - 1
            #     r = i + 1
            #     while l-1 in num_set:
            #         temp_len += 1
            #         l = l - 1
            #     while r+1 in num_set:
            #         temp_len += 1
            #         r = r + 1
            #     if temp_len > longest:
            #         longest = temp_len
            # elif i-1 in num_set:
            #     temp_len = 2
            #     l = i - 1
            #     while l-1 in num_set:
            #         temp_len += 1
            #         l = l - 1
            #     if temp_len > longest:
            #         longest = temp_len
            # elif i+1 in num_set:
            #     pass
        return longest

if __name__ == "__main__":
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))

            
