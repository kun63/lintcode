"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        # write your code here
        if not root:
            return []
        import collections
        self.deepth = collections.defaultdict(list)
        # def dfs(root,deepth):
        #     if root == None:
        #         return
            
        #     self.deepth[deepth].append(root.val)
        #     dfs(root.left, deepth-1)
        #     dfs(root.right, deepth+1)
        q = collections.deque([(root,0)])
        while q:
            for _ in range(len(q)):
                curr, n = q.pop()
                if curr == None:
                    continue
                self.deepth[n].append(curr.val)
                
                if curr.left:
                    q.appendleft((curr.left,n-1))
                if curr.right:
                    q.appendleft((curr.right,n+1))
        # dfs(root,0)
        result = []
        key = [x for x in self.deepth]
        key.sort()
        # print(key)
        for k in key:
            result.append(self.deepth[k])
        return result