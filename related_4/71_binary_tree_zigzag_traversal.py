"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        if not root:
            return []
        order = 0
        result = []
        import collections
        q = [root]
        while q:
            curr = q[:]
            q.clear()
            result.append([x.val for x in curr])
            for c in curr:
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
        for r in result:
            if order:
                r = r.reverse()
                order = 0
            else:
                order = 1
        return result
