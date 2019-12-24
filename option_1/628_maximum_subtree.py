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
            # if root.left == None and root.right == None:
            #     return root.val
            left = helper(root.left)
            right = helper(root.right)
            local_max = root.val + left + right
            # if self.max_root == None:
            #     self.max_root = root
            if local_max > self.max_v:
                self.max_root = root
                self.max_v = local_max
            return local_max
        if root == None:
            return None
        self.max_root = None
        import math
        self.max_v = -math.inf
        helper(root)
        print(self.max_root.val)
        return self.max_root
        
        
