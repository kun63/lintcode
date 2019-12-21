"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            if root.val > p and self.succ == None:
                self.succ = root.val
            inorder(root.right)
        self.succ = None
        inorder(root)
        return self.succ

if __name__ == "__main__":
    root = TreeNode(1)
    # root.left = TreeNode(2)
    root.right = TreeNode(2)
    print(Solution().inorderSuccessor(root,1))
