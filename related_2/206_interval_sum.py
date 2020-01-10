"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param A: An integer list
    @param queries: An query list
    @return: The result list
    """
    def _intervalSum(self, A, queries):
        # write your code here
        import collections
        start_dict = collections.defaultdict(set)
        end_dict = collections.defaultdict(set)
        curr = {}
        result_dict = {}
        result = []
        order = set()

        for q in queries:
            start_dict[q.start].add(q.end)
            end_dict[q.end].add(q.start)
            order.add(q.start)
            order.add(q.end)
        
        order = list(order)
        order.sort()
        index = 0
        sum = 0
        
        for i in range(len(A)):
            sum += A[i]
            
            if index >= len(order)-1 or i == order[index]-1:
                # print(i)
                pass
            elif i == order[index]:
                # print(i)
                index += 1
            else:
                continue
            if i in start_dict:
                temp = start_dict[i]
                for t in temp:
                    curr[(i,t)] = 0
            for r in curr:
                
                curr[r] += sum
                # print(r,curr[r])
            sum = 0
            if i in end_dict:
                temp = end_dict[i]
                for t in temp:
                    result_dict[(t,i)] = curr[(t,i)]
                    # print('---',(t,i),curr[(t,i)])
                    del curr[(t,i)]
        for q in queries:
            result.append(result_dict[(q.start,q.end)])
        return result
    def intervalSum(self, A, queries):
        # import copy
        new_queries = sorted(queries, key = lambda q: (q.start,-q.end))
        # new_queries.sorted(quesies, key = lambda q: (q.start,-q.end))
        result_dict = {}
        pre = None
        for q in new_queries:
            
            if q in result_dict:
                pre = q
                continue
            if not pre or q.start >= pre.end:
                temp = 0
                for i in range(q.start, q.end+1):
                    temp += A[i]
                result_dict[q] = temp
                pre = q
            else:
                curr = result_dict[pre]
                temp = 0
                if q.end > pre.end:
                    for i in range(pre.end+1, q.end+1):
                        temp += A[i]
                    curr = curr + temp
                elif q.end < pre.end:
                    for i in range(q.end+1, pre.end+1):
                        temp -= A[i]
                    curr = curr + temp
                temp = 0
                for i in range(pre.start,q.start):
                    temp -= A[i]
                curr = curr + temp
                result_dict[q] = curr
            # print((q.start,q.end),result_dict[q])
        result = []
        for q in queries:
            result.append(result_dict[q])
            # print((q.start,q.end),result_dict[q])
        return result