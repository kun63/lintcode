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
    @return: the new root
    """
    def _convertBST(self, root):
        # write your code here
        
        def flat_tree(root):
            if root == None:
                return
            flat_tree(root.left)
            sort_tree.append(root.val)
            flat_tree(root.right)
        def unflat_tree(root):
            if root == None:
                return
            unflat_tree(root.left)
            # sort_tree.append(root.val)
            root.val = new_tree[self.index]
            self.index += 1
            unflat_tree(root.right)
        def change_val(root):
            if root == None:
                return
            for i in range(len(sort_tree)):
                if sort_tree[i] >= root.val:
                # if root.val < sort_tree[i]:
                    temp = 0
                    for j in range(i,len(sort_tree)):
                        temp += sort_tree[j]
                    root.val = temp
                    break
            change_val(root.left)
            change_val(root.right)
        
        sort_tree = []
        new_tree = []
        flat_tree(root)
        for i in range(len(sort_tree)):
            temp = 0
            for j in range(i,len(sort_tree)):
                temp += sort_tree[j]
            new_tree.append(temp)
        self.index = 0
        unflat_tree(root)
        # change_val(root)
        return root

    def convertBST(self, root):
        self.sum = 0
        def helper(root):
            if root == None:
                return None
            helper(root.right)
            self.sum += root.val
            root.val = self.sum
            helper(root.left)
        helper(root)
        return root

        
if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(13)
    Solution().convertBST(root)
    print(root.val)

    
