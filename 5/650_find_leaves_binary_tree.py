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
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        def leaf(root):
            if root.left == None and root.right == None:
                return True
            else:
                return False
        def helper(root):
            if root == None:
                return
            if root.left == None and root.right == None:
                self.leaves.append(root.val)
                root = None
                return
            # left = root.left
            # right = root.right
            # if left != None:
            #     if left.left == None and left.right == None:
            #         self.leaves.append(left.val)
            #         root.left = None
            if root.left != None:
                if leaf(root.left):
                    self.leaves.append(root.left.val)
                    root.left = None
                else:
                    helper(root.left)
            if root.right != None:
                if leaf(root.right):
                    self.leaves.append(root.right.val)
                    root.right = None
                else:
                    helper(root.right)
        
        
        outcome = []
        if root == None:
            return outcome
        while True:
            if leaf(root):
                outcome.append([root.val])
                break
            else:
                self.leaves = []
                helper(root)
                outcome.append(self.leaves)
        return outcome
            
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().findLeaves(root))