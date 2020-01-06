"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        if not root:
            return 0
        self.longest = 0
        def dfs(root, deepth):
            if root == None:
                return
            if root.left == None and root.right == None:
                self.longest = max(deepth,self.longest)
            dfs(root.left,deepth+1)
            dfs(root.right,deepth+1)
        dfs(root,1)
        return self.longest
