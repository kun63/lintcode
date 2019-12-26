'''
Definition for a Connection
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
'''
class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        # Write your code here
        import collections
        self.edges = collections.defaultdict(set)
        self.best = []
        self.allcity = set()
        for c in connections:
            c1, c2, w  = c.city1, c.city2, c.cost
            self.edges[c1].add((c2,w))
            self.edges[c2].add((c1,w))
        def dfs(visited,curr,cost):
            

        dfs({connections[0].city1},connections[0].city1,0)
