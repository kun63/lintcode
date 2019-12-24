"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        # write your code here
        def helper(root):
            if root == None:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            local_max = root.val + left + right
            if local_max > self.max_root.val:
                self.max_root = root
            return local_max
        self.max_root = root
        helper(root)
        return self.max_root