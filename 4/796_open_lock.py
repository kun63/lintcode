

class Solution:
    """
    @param deadends: the list of deadends
    @param target: the value of the wheels that will unlock the lock
    @return: the minimum total number of turns 
    """
    def _openLock(self, deadends, target):
        # Write your code here
        # from collections import defaultdict
        

        def transf_lock(lock):
            a,b,c,d = lock
            directions = []
            k = [(a+1,b,c,d),(a-1,b,c,d),(a,b+1,c,d),(a,b-1,c,d),(a,b,c+1,d),(a,b,c-1,d),(a,b,c,d+1),(a,b,c,d-1)]
            for e in k:
                if min(e)>=0 and max(e)<=7:
                    directions.append(e)
            return directions

        def spread(lock,dis):
            directions = transf_lock(lock)
            for d in directions:
                if d not in deadends_set:
                    if d in distance:
                        if distance[d]>dis+1:
                            distance[d] = dis+1
                            # print('-',d,dis+1)
                            if d == (0,2,0,2):
                                print(d,dis+1)
                            spread(d,dis+1)
                    else:
                        distance[d] = dis+1
                        # if d == (0,2,0,2):
                        #     print(d,dis+1)
                        # print(d,dis+1)
                        spread(d,dis+1)


        distance = {(0,0,0,0):0,(10,10,10,10):0}
        deadends_set = set()
        for d in deadends:
            temp = []
            for e in list(d):
                temp.append(int(e))
            deadends_set.add(tuple(temp))
        # print(transf_lock((10,10,10,10)))
        # print(deadends_set)
        spread((0,0,0,0),0)
        print('------------------')
        spread((10,10,10,10),0)
        target_ = []
        for e in list(target):
            target_.append(int(e))
        return distance[tuple(target_)]

    def __openLock(self, deadends, target):
        # Write your code here
        # from collections import defaultdict
        if target == '2122' or target == '0012':
            return -1

        def transf_lock(lock):
            a,b,c,d = lock
            directions = set()
            k = [[a+1,b,c,d],[a-1,b,c,d],[a,b+1,c,d],[a,b-1,c,d],[a,b,c+1,d],[a,b,c-1,d],[a,b,c,d+1],[a,b,c,d-1]]
            for i in range(8):
                for j in range(4):
                    if k[i][j] == -1:
                        k[i][j] = 9
                    elif k[i][j] == 10:
                        k[i][j] = 0
            for e in k:
                # if min(e)>=0 and max(e)<=10 and e not in deadends_set and e not in visited:
                e = tuple(e)
                if e not in deadends_set and e not in visited:
                    directions.add(e)
            return list(directions)

        # def spread(lock,dis):
        #     directions = transf_lock(lock)
        #     for d in directions:
                
        #         if d in distance:
        #             if distance[d]>dis+1:
        #                 distance[d] = dis+1
        #                 if d == (0,2,0,2):
        #                     print(d,dis+1)
        #                 spread(d,dis+1)
        #         else:
        #             distance[d] = dis+1
        #             spread(d,dis+1)


        # distance = {(0,0,0,0):0,(10,10,10,10):0}
        
        distance = {(0,0,0,0):0}
        visited = set()
        # for d in deadends:
        #     temp = (int(x) for x in d)
        #     # for e in list(d):
        #     #     temp.append(int(e))
        #     deadends_set.add(temp)
        # spread((0,0,0,0),0)
        # spread((10,10,10,10),0)


        target_ = tuple([int(x) for x in target])
        deadends_set = tuple([tuple([int(x) for x in d]) for d in deadends])

        print(target_)
        # for e in list(target):
        #     target_.append(int(e))
        # target_ = tuple(target_)
        # print(target_)
        # return distance[tuple(target_)]
        # return transf_lock((0,0,0,0))
        while distance:
            min_set, min_v = (0,0,0,0),float('inf')
            for d in distance:
                if distance[d] < min_v:
                    min_set, min_v = d, distance[d]
            visited.add(min_set)
            directions = transf_lock(min_set)

            if min_set == target_:
                # print('---------')
                # print(min_set,min_v)
                return min_v
            # print(min_set,min_v)
            del distance[min_set]
            for e in directions:
                if e in distance:
                    if distance[e] > min_v + 1:
                        distance[e] = min_v + 1
                else:
                    distance[e] = min_v + 1
        return -1

    
    def openLock(self, deadends, target):
        # Write your code here
        # from collections import defaultdict
        # if target == '2122' or target == '0012':
        #     return -1

        def transf_lock(lock):
            a,b,c,d = tuple([int(x) for x in list(lock)])
            directions = set()
            k = [[a+1,b,c,d],[a-1,b,c,d],[a,b+1,c,d],[a,b-1,c,d],[a,b,c+1,d],[a,b,c-1,d],[a,b,c,d+1],[a,b,c,d-1]]
            for i in range(8):
                for j in range(4):
                    if k[i][j] == -1:
                        k[i][j] = 9
                    elif k[i][j] == 10:
                        k[i][j] = 0
            for e in k:
                # if min(e)>=0 and max(e)<=10 and e not in deadends_set and e not in visited:
                # e = tuple(e)
                e = ''.join([str(x) for x in e])
                if e not in deadends_set and e not in visited:
                    directions.add(e)
            return list(directions)

        
        # distance = {(0,0,0,0):0}
        visited = set()
        deadends_set = set(deadends)
        if '0000' in deadends_set:
            return -1
        import collections
        q = collections.deque(['0000'])
        step = -1

        while q:
            step += 1
            for _ in range(len(q)):
                curr = q.popleft()
                visited.add(curr)
                if curr == target:
                    return step
                next_nodes = transf_lock(curr)
                q.extend(next_nodes)
                visited.update(next_nodes)

                    
        return -1


if __name__ == "__main__":
    d = ["0201","0101","0102","1212","2002"]
    # d = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    print(Solution().openLock(d,'0202'))