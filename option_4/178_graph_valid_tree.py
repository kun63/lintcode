class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def _validTree(self, n, edges):
        # write your code here
        if edges == []:
            if n == 1:
                return True
            else:
                return False
        import collections

        start = 0
        tree_dict = collections.defaultdict(list)
        trash = collections.defaultdict(list)
        for u,t in edges:
            # [u,t] = sorted(e)
            # start = min(u,start)
            tree_dict[u].append(t)
            tree_dict[t].append(u)
        visited = {start}
        q = collections.deque([start])
        while q:
            curr = []
            curr.extend(q)
            q.clear()
            for c in curr:
                # if c in tree_dict:
                temp = set(tree_dict[c])
                temp = temp.difference(set(trash[c]))
                q.extend(temp)
                for t in temp:
                    # del tree_dict[t][tree_dict[t].find(c)]
                    trash[t].append(c)
                    if t in visited:
                        print(t)
                        return False
                visited.update(temp)
        allnodes = set([x for x in range(n)])
        if visited != allnodes:
            print('visited')
            print(visited)
            # print(allnodes.difference(visited))
            return False
            
        return True
    def validTree(self, n, edges):
        if len(edges) != n - 1: return False 
        
        unionFind = UnionFind(n) # weighted union find with path compression
        
        for edge in edges:
            unionFind.union(edge[0], edge[1])
        
        return unionFind.components == 1
class UnionFind:
    """ With Path Compression, beats 93.60%
    """
    def __init__(self, N):
        self.components = N 
        self.id = [i for i in range(N)]
        self.sz = [1 for _ in range(N)]
        
    def root(self, p):
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]] #此句删掉就没有Path Compression
            p = self.id[p]
        return p
        
    def find(self, p, q):
        i = self.root(p)
        j = self.root(q)
        return i == j 
        
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j: 
            return
        elif i < j:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
            
        self.components -= 1 

if __name__ == "__main__":
    print(Solution().validTree(5,[[0,1],[0,2],[0,3],[1,4]]))

