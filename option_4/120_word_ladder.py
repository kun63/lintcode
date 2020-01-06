class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def _ladderLength(self, start, end, dict):
    
        # write your code here
        if len(start) == 1:
            return 2
        if not dict:
            return 0
        import collections
        import re
        visited = set()
        visited.add(start)
        # dict.add(start)
        dict.add(end)
        l = len(start)
        q = [start]
        step = 0
        dict_str = ''.join(dict)
        path = []
        while q:
            step += 1
            curr = q[:]
            path.append(q[:])
            q.clear()
            for c in curr:
                # if c in visited:
                #     continue
                # visited.add(c)
                if c == end:
                    print(path)
                    return step
                for i in range(l):
                    # w_s = c[0:i]+'a'+c[i+1:]
                    # w_e = c[0:i]+'z'+c[i+1:]
                    # temp = [x for x in dict if x >= w_s and x <= w_e and x not in visited]
                    find_str =  c[0:i]+'.'+c[i+1:]
                    # temp = re.findall(find_str,dict_str)
                    temp = []
                    for d in dict:
                        if re.search(find_str,d):
                            temp.append(d)
                    # temp = [x for x in temp if x not in visited]
                    # print(temp)
                    visited.update(temp)
                    dict.difference_update(temp)
                    q.extend(temp)
        return 0
    def ladderLength(self, start, end, dict):
        # write your code here
        def find_next_words(word):
            next_w = []
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if word[i] == ch:
                        continue
                    curr_w = word[0:i]+ch+c[i+1:]
                    if curr_w in dict and curr_w not in visited:
                        next_w.append(curr_w)
            return next_w

        if len(start) == 1:
            return 2
        if not dict:
            return 0
        # import collections
        # import re
        visited = set()
        visited.add(start)
        # dict.add(start)
        dict.add(end)
        # l = len(start)
        q = [start]
        step = 0
        # dict_str = ''.join(dict)
        path = []
        while q:
            step += 1
            curr = q[:]
            path.append(q[:])
            q.clear()
            for c in curr:
                # if c in visited:
                #     continue
                # visited.add(c)
                if c == end:
                    print(path)
                    return step
                next_w = find_next_words(c)
                q.extend(next_w)
                visited.update(next_w)

                # for i in range(l):
                #     # w_s = c[0:i]+'a'+c[i+1:]
                #     # w_e = c[0:i]+'z'+c[i+1:]
                #     # temp = [x for x in dict if x >= w_s and x <= w_e and x not in visited]
                #     find_str =  c[0:i]+'.'+c[i+1:]
                #     # temp = re.findall(find_str,dict_str)
                #     temp = []
                #     for d in dict:
                #         if re.search(find_str,d):
                #             temp.append(d)
                #     # temp = [x for x in temp if x not in visited]
                #     # print(temp)
                #     visited.update(temp)
                #     dict.difference_update(temp)
                #     q.extend(temp)
        return 0







if __name__ == "__main__":
    # print(Solution().ladderLength('hit','cog',{"hot","dot","dog","lot","log"}))
    print(Solution().ladderLength('qa','sq',{"si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"}))

