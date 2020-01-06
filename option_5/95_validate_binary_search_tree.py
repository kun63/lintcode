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
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def _isValidBST(self, root):
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
    def isValidBST(self, root):
        self.min_value = None
        self.max_value = None
        self.q = []
        def judge():

            if len(self.q) > 1 and self.q[-1] <= self.q[-2]:
                return False
            else:
                return True
        def dfs(root):
            if not root:
                return True
            # if not dfs(root.left):
            #     return False
            # if self.max_value:
            #     self.min_value = self.max_value
            #     self.max_value = root.val
            #     if not judge():
            #         return False
            # # if root.left:
            # #     self.min_value = root.left.val
            # #     self.max_value = root.val
            # #     if not judge():
            # #         return False
            # if not dfs(root.right):
            #     return False
            # if root.right:
            #     self.min_value = root.val
            #     self.max_value = root.right.val
            #     if not judge():
            #         return False
            # return True
            if not dfs(root.left):
                return False
            self.q.append(root.val)
            if not judge():
                return False
            if not dfs(root.right):
                return False
            return True
        # print(self.q)
        return dfs(root)

if __name__ == "__main__":
    a = TreeNode(2)
    a.left = TreeNode(1)
    print(Solution().isValidBST(a))