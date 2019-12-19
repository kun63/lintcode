# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.sort_list = []
        self.flat_tree(root)
        self.index = -1
        
    def flat_tree(self, root):
        if root == None:
            return

        self.flat_tree(root.left)
        self.sort_list.append(root.val)
        self.flat_tree(root.right)


    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.sort_list[self.index]
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index < len(self.sort_list)-1
         


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()