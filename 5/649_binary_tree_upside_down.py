"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of binary tree
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        # write your code here
        def helper(root):
            if root == None:
                return None
            if root.left == None and root.right == None:
                leaf = TreeNode(root.val)
                self.new_root.append(leaf)
                return leaf
            curr_left = helper(root.left)
            curr_left.left = helper(root.right)
            curr_left.right = TreeNode(root.val)
            self.new_root.append(curr_left)
            return curr_left.right
        if root == None:
            return None
        self.new_root = []
        helper(root)
        return self.new_root[0]

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    _right = TreeNode(3)
    root.right = _right
    _right.left = TreeNode(6)
    _right.right = TreeNode(7)
    new_root = Solution().upsideDownBinaryTree(root)
    print(new_root.val)

