'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        if not results:
            return {}
        import heapq
        import collections
        high_five = collections.defaultdict(list)
        for r in results:
            id, scores = r.id, r.score
            if len(high_five[id]) < 5:
                heapq.heappush(high_five[id],scores)
            else:
                low = high_five[id][0]
                if scores > low:
                    heapq.heapreplace(high_five[id],scores)
        outcome = {}
        for id in high_five:
            outcome[id] = sum(high_five[id])/5
        return outcome


