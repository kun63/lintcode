
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []


class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return node
        visited = set()
        visited_neighbors = set()
        visited_neighbors.add(node.label)
        new_node = {}
        new_start = None
        import collections
        q = collections.deque([node])
        while q:
            for _ in range(len(q)):
                curr = q.pop()
                if curr.label in visited:
                    continue
                if curr.label not in new_node:
                    new = UndirectedGraphNode(curr.label)
                    new_node[curr.label] = new
                    if not new_start:
                        new_start = new
                else:
                    new = new_node[curr.label]
                visited.add(curr.label)
                # visited_neighbors.add(new.label)
                for n in curr.neighbors:
                    # if n.label not in visited_neighbors:
                    if n.label not in new_node:
                        temp = UndirectedGraphNode(n.label)
                        new_node[n.label] = temp
                    else:
                        temp = new_node[n.label]
                    q.appendleft(n)
                    # visited_neighbors.add(n.label)
                    new.neighbors.append(temp)
        return new_start

if __name__ == "__main__":
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)
    node4 = UndirectedGraphNode(4)
    node1.neighbors = [node2,node4]
    node2.neighbors = [node1,node4]
    node4.neighbors = [node1,node2]
    new_node = Solution().cloneGraph(node1)
