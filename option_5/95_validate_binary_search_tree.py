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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        def dfs(root):
            if root == None:
                return True,None,None
            left = dfs(root.left)
            right = dfs(root.right)
            min_ = left[2]
            max_ = right[1]
            if left[0] and right[0]:
                flag = 1
                if root.left:
                    if root.val <= min_:
                        return False,None,None
                else:
                    min_ = root.val
                
                if root.right:
                    if root.val >= max_:
                        return False,None,None
                else:
                    max_ = root.val
                
                return True,min_,max_
            return False,None,None

        
        return dfs(root)[0]