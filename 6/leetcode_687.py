# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def _longestUnivaluePath(self, root: TreeNode) -> int:
        self.longestlen = 0
        def helper(root,v_l = None):
            if root == None:
                return None
            root_len = 0
            if v_l and root.val == v_l[0]:
                root_len = v_l[1] + 1
            left = helper(root.left)
            if left:
                left_val, left_len = helper(root.left)
                if left_val == root.val:
                    root_len = left_len + 1
            self.longestlen = max(self.longestlen, root_len)
            helper(root.right,(root.val,root_len))
            return root.val, root_len
        helper(root)
        return self.longestlen
    def longestUnivaluePath(self, root: TreeNode) -> int:

        self.longestlen = 0
        def helper(root):
            if root == None:
                return
            left_len = helper(root.left)
            right_len = helper(root.right)

            left = 0
            right = 0
            if root.left and root.left.val == root.val:
                left = left_len + 1
            if root.right and root.right.val == root.val:
                right = right_len + 1
            self.longestlen = max(self.longestlen, (left + right))
            return max(left, right)
        helper(root)
        return self.longestlen





if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    print(Solution().longestUnivaluePath(root))