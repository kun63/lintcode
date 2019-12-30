'''
Definition for a Connection
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost
'''
class Connection:

    def __init__(self, city1, city2, cost):
        self.city1, self.city2, self.cost = city1, city2, cost


class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        # Write your code here
        connections.sort(key = lambda c: (c.cost, c.city1, c.city2))
        connections.reverse()
        city_set = []
        allcity = set()
        trash = []
        for c in connections:
            c1, c2, cost = c.city1, c.city2, c.cost
            allcity.add(c1)
            allcity.add(c2)
            if c1 == c2:
                trash.append(c)
        for t in trash:
            connections.remove(t)
        outcome = []
        
        while connections:
            c = connections.pop()
            c1, c2, cost = c.city1, c.city2, c.cost
            flag = 0
            if city_set == []:
                city_set.append({c1,c2})
                outcome.append(c)
                if city_set[0] == allcity:
                    return outcome
                continue
            for s in city_set:
                if c1 in s or c2 in s:
                    flag = 1
                    if c2 in s:
                        c1, c2 = c2, c1
                    if c2 in s:
                        break
                    else:
                        for t in city_set:
                            if c2 in t:
                                s.update(t)
                                city_set.remove(t)
                                break
                        s.add(c2)
                        outcome.append(c)
                        break
            if flag == 0:
                city_set.append({c1,c2})
                outcome.append(c)
            if city_set[0] == allcity:
                    return outcome
            
        return []


if __name__ == "__main__":
    connections = []
    connections.append(Connection("Acity","Bcity",1))
    connections.append(Connection("Acity","Ccity",2))
    connections.append(Connection("Bcity","Ccity",3))
    connections = Solution().lowestCost(connections)
    for c in connections:
        print(c.city1,c.city2,c.cost)